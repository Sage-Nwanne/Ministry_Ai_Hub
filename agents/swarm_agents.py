from swarms import Agent
from swarms.models import OpenAIChat
import os
import json
import random
import hashlib
from typing import Optional
from dotenv import load_dotenv
from agents.utils import setup_logging, get_redis_client

load_dotenv()
logger = setup_logging()
redis_client = get_redis_client()

# Fix the model initialization to handle missing API key gracefully
def initialize_model():
    """Initialize OpenAI model with proper error handling"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("OPENAI_API_KEY not found. Some features may not work.")
        return None
    
    try:
        from swarms.models import OpenAIChat
        model = OpenAIChat(
            openai_api_key=api_key,
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=500
        )
        logger.info("OpenAI model initialized successfully for Swarms")
        return model
    except Exception as e:
        logger.error(f"Failed to initialize OpenAI model: {str(e)}")
        return None

model = initialize_model()

# Add fallback for when model is None
if not model:
    logger.warning("Running without OpenAI model - using fallback responses")

# Escalation Detection Agent
escalation_agent = Agent(
    agent_name="EscalationDetector",
    system_prompt="""You are an escalation detection specialist for a ministry. 
    Analyze messages for sensitive topics requiring human intervention including: 
    suicidal thoughts, severe depression, abuse, violence, self-harm, or urgent medical needs.
    
    Respond with only 'ESCALATE' or 'NORMAL'.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Scripture Recommendation Agent  
scripture_agent = Agent(
    agent_name="ScriptureRecommender",
    system_prompt="""You are a biblical scholar and pastoral counselor. 
    Based on user messages, recommend appropriate scripture verses that provide 
    comfort, guidance, or wisdom. Return only the verse reference and text.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Tone Polishing Agent (Dr. Myles)
tone_agent = Agent(
    agent_name="DrMylesPolisher", 
    system_prompt="""You are Dr. Myles, a compassionate and wise spiritual leader.
    Your role is to rewrite responses in a pastoral, encouraging tone that incorporates
    scripture naturally. Be warm, empathetic, and spiritually grounding.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

def load_verses():
    """Load verses from data/verses.json with fallback"""
    try:
        with open("data/verses.json", "r") as f:
            verses = json.load(f)
            logger.info(f"Loaded {len(verses)} verses from verses.json")
            return verses
    except Exception as e:
        logger.error(f"Failed to load verses.json: {str(e)}")
        return [
            {
                "reference": "Proverbs 3:5-6",
                "text": "Trust in the Lord with all your heart, and do not lean on your own understanding."
            },
            {
                "reference": "Philippians 4:13", 
                "text": "I can do all things through Christ who strengthens me."
            }
        ]

VERSES = load_verses()

def get_random_scripture():
    """Get a random scripture verse"""
    verse = random.choice(VERSES)
    return f"{verse['reference']} - {verse['text']}"

def detect_escalation_swarm(message: str) -> bool:
    """Use swarms agent for escalation detection with caching"""
    cache_key = "escalation:" + hashlib.sha256(message.encode()).hexdigest()
    
    try:
        # Check cache first
        if redis_client:
            cached = redis_client.get(cache_key)
            if cached:
                result = cached.decode('utf-8') if isinstance(cached, bytes) else cached
                return "ESCALATE" in result.upper()
        
        # Run escalation detection
        prompt = f"""
        Analyze this message for escalation needs. Respond with "ESCALATE" if the message contains:
        - Suicidal thoughts or self-harm
        - Abuse situations
        - Mental health crises
        - Urgent pastoral care needs
        
        Message: {message}
        """
        
        result = escalation_agent.run(prompt)
        
        # Cache result if Redis available
        if redis_client:
            redis_client.setex(cache_key, 86400, str(result))
        
        escalate = "ESCALATE" in str(result).upper()
        logger.info(f"Escalation check: {escalate} for message: {message[:50]}...")
        return escalate
        
    except Exception as e:
        logger.error(f"Escalation detection error: {str(e)}")
        return True  # Fail safe - escalate on error

def get_scripture_recommendation_swarm(message: str) -> str:
    """Use swarms agent for scripture recommendation with caching"""
    cache_key = "scripture:" + hashlib.sha256(message.encode()).hexdigest()
    
    try:
        # Check cache first
        cached = redis_client.get(cache_key)
        if cached:
            result = cached.decode('utf-8') if isinstance(cached, bytes) else cached
            return result
        
        # Get scripture recommendation
        result = scripture_agent.run(f"Recommend appropriate scripture for: {message}")
        
        # Cache result
        redis_client.setex(cache_key, 86400, result)
        
        logger.info(f"Scripture recommended for: {message[:50]}...")
        return str(result)
        
    except Exception as e:
        logger.error(f"Scripture recommendation error: {str(e)}")
        return get_random_scripture()

def polish_response_swarm(raw_response: str, context: str = "", scripture: str = "") -> str:
    """Use swarms agent for tone polishing with caching"""
    if not scripture:
        scripture = get_random_scripture()
    
    prompt = f"""
    Context: {context}
    Scripture to incorporate: {scripture}
    Original Response: {raw_response}
    
    Rewrite this response as Dr. Myles would say it, incorporating the scripture naturally 
    in a warm, pastoral tone.
    """
    
    cache_key = "tone:" + hashlib.sha256(prompt.encode()).hexdigest()
    
    try:
        # Check cache first
        cached = redis_client.get(cache_key)
        if cached:
            result = cached.decode('utf-8') if isinstance(cached, bytes) else cached
            return result
        
        # Polish the response
        result = tone_agent.run(prompt)
        
        # Cache result
        redis_client.setex(cache_key, 86400, result)
        
        logger.info(f"Response polished for context: {context}")
        return str(result)
        
    except Exception as e:
        logger.error(f"Tone polishing error: {str(e)}")
        return raw_response

# FAQ Response Agent
faq_agent = Agent(
    agent_name="FAQResponder",
    system_prompt="""You are a ministry FAQ specialist. When provided with FAQ content,
    enhance and format it appropriately for the user while maintaining accuracy and helpfulness.
    Make the response warm and pastoral in tone.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

def process_faq_response_swarm(faq_answer: str, user_question: str) -> str:
    """Use swarms agent to enhance FAQ responses"""
    cache_key = "faq_enhanced:" + hashlib.sha256((faq_answer + user_question).encode()).hexdigest()
    
    try:
        # Check cache first
        cached = redis_client.get(cache_key)
        if cached:
            result = cached.decode('utf-8') if isinstance(cached, bytes) else cached
            return result
        
        # Enhance the FAQ response
        prompt = f"""
        User Question: {user_question}
        FAQ Answer: {faq_answer}
        
        Enhance this FAQ answer to be more pastoral and helpful while keeping the core information accurate.
        """
        
        result = faq_agent.run(prompt)
        
        # Cache result
        redis_client.setex(cache_key, 86400, result)
        
        logger.info(f"FAQ response enhanced for: {user_question[:50]}...")
        return str(result)
        
    except Exception as e:
        logger.error(f"FAQ enhancement error: {str(e)}")
        return faq_answer  # Return original if enhancement fails

# Export functions
__all__ = [
    'detect_escalation_swarm',
    'get_scripture_recommendation_swarm', 
    'polish_response_swarm',
    'process_faq_response_swarm',
    'escalation_agent',
    'scripture_agent', 
    'tone_agent',
    'faq_agent'
]
