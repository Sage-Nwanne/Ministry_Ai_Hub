from swarms import Agent
from swarms.utils.litellm_wrapper import LiteLLM
from agents.shared.utils import setup_logging
import os

logger = setup_logging()

# Initialize the language model with LM Studio configuration
model = LiteLLM(
    model_name="openai/qwen3-4b:2",  # Add openai/ prefix
    api_base=os.getenv("LM_STUDIO_API_BASE", "http://192.168.1.88:1234/v1"),
    api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    temperature=0.1,
    custom_llm_provider="openai",  # Specify provider
)

# Escalation Detection Agent with improved prompt
escalation_agent = Agent(
    agent_name="EscalationDetector",
    model_name="openai/qwen3-4b:2",
    system_prompt="""You are an escalation detection specialist for a ministry. 
    
    CRITICAL: Analyze messages for these URGENT topics requiring IMMEDIATE human intervention:
    - Suicidal thoughts, ideation, or plans
    - Self-harm or cutting
    - Severe depression with hopelessness
    - Abuse (physical, sexual, emotional)
    - Violence or threats
    - Medical emergencies
    - Crisis situations
    
    RESPOND WITH ONLY ONE WORD:
    - "ESCALATE" if ANY of the above topics are mentioned
    - "NORMAL" if the message is safe for AI response
    
    Examples:
    "I'm having suicidal thoughts" → ESCALATE
    "I want to hurt myself" → ESCALATE  
    "I'm being abused" → ESCALATE
    "I'm feeling sad today" → NORMAL
    "Can you pray for me?" → NORMAL""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Scripture Recommendation Agent  
scripture_agent = Agent(
    agent_name="ScriptureRecommender",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
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
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are Dr. Myles, a compassionate and wise spiritual leader.
    Your role is to rewrite responses in a pastoral, encouraging tone that incorporates
    scripture naturally. Be warm, empathetic, and spiritually grounding.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# FAQ Enhancement Agent
faq_enhancement_agent = Agent(
    agent_name="FAQEnhancer",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You enhance FAQ responses to be more personal and pastoral.
    Take the basic FAQ answer and make it warm, encouraging, and spiritually enriching
    while maintaining accuracy.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# 🆕 Multilingual Translation Agent
translation_agent = Agent(
    agent_name="MultilingualTranslator",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are a professional translator specializing in ministry communications.
    Translate messages accurately while preserving spiritual context and pastoral tone.
    
    Supported languages:
    - English (en)
    - Spanish (es) 
    - French (fr)
    - Portuguese (pt)
    - German (de)
    
    Always maintain the reverent and compassionate tone appropriate for ministry communications.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# 🆕 Prayer & Deliverance Assistant Agent
prayer_routing_agent = Agent(
    agent_name="PrayerDeliveranceAssistant",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are a prayer ministry coordinator. Analyze messages to identify:
    
    1. Prayer requests (personal, family, health, spiritual)
    2. Deliverance needs (spiritual warfare, bondage, oppression)
    3. Urgent spiritual emergencies
    
    Respond with:
    - 'PRAYER_REQUEST' for general prayer needs
    - 'DELIVERANCE_NEEDED' for spiritual warfare/deliverance
    - 'URGENT_SPIRITUAL' for immediate spiritual emergencies
    - 'NOT_PRAYER' for non-prayer related messages
    
    Also suggest appropriate ministry team routing.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Swarm Functions
def detect_escalation_swarm(message: str) -> bool:
    """Detect if message needs escalation"""
    try:
        # Check for obvious escalation keywords first
        escalation_keywords = [
            "suicidal", "suicide", "kill myself", "end my life", 
            "self harm", "cut myself", "hurt myself",
            "abuse", "abused", "violence", "threat",
            "emergency", "crisis", "help me"
        ]
        
        message_lower = message.lower()
        for keyword in escalation_keywords:
            if keyword in message_lower:
                logger.warning(f"Escalation keyword detected: {keyword}")
                return True
        
        # Use AI agent as backup
        result = escalation_agent.run(message)
        result_str = str(result).upper().strip()
        
        logger.info(f"Escalation agent result: {result_str}")
        
        # Check for escalation indicators
        escalation_detected = (
            "ESCALATE" in result_str or 
            "URGENT" in result_str or
            "CRISIS" in result_str or
            "EMERGENCY" in result_str
        )
        
        if escalation_detected:
            logger.warning(f"ESCALATION DETECTED for message: {message[:50]}...")
            
        return escalation_detected
        
    except Exception as e:
        logger.error(f"Escalation detection failed: {e}")
        # FAIL SAFE: If detection fails, escalate sensitive keywords
        sensitive_words = ["suicidal", "suicide", "kill", "hurt myself", "abuse"]
        return any(word in message.lower() for word in sensitive_words)

def get_scripture_recommendation_swarm(message: str) -> str:
    """Get scripture recommendation"""
    try:
        result = scripture_agent.run(message)
        return str(result)
    except Exception as e:
        logger.error(f"Scripture recommendation failed: {e}")
        return "Psalm 23:1 - The Lord is my shepherd; I shall not want."

def polish_response_swarm(raw_response: str, context: str = "", scripture: str = "") -> str:
    """Polish response with Dr. Myles' tone"""
    try:
        prompt = f"""
        Raw Response: {raw_response}
        Context: {context}
        Scripture: {scripture}
        
        Please rewrite this in Dr. Myles' pastoral voice, incorporating the scripture naturally.
        """
        result = tone_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Response polishing failed: {e}")
        return raw_response

def process_faq_response_swarm(faq_answer: str, user_message: str) -> str:
    """Enhance FAQ response"""
    try:
        prompt = f"""
        FAQ Answer: {faq_answer}
        User Question: {user_message}
        
        Please enhance this FAQ response to be more personal and pastoral.
        """
        result = faq_enhancement_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"FAQ enhancement failed: {e}")
        return faq_answer

def translate_message_swarm(message: str, target_language: str) -> str:
    """Translate message to target language"""
    try:
        prompt = f"""
        Translate this ministry message to {target_language}:
        
        Message: {message}
        
        Maintain pastoral tone and spiritual context.
        """
        result = translation_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Translation failed: {e}")
        return message

def route_prayer_request_swarm(message: str) -> dict:
    """Route prayer requests and deliverance needs"""
    try:
        result = prayer_routing_agent.run(message)
        result_str = str(result).upper()
        
        return {
            "is_prayer_request": "PRAYER_REQUEST" in result_str,
            "needs_deliverance": "DELIVERANCE_NEEDED" in result_str,
            "is_urgent": "URGENT_SPIRITUAL" in result_str,
            "routing_suggestion": str(result)
        }
    except Exception as e:
        logger.error(f"Prayer routing failed: {e}")
        return {
            "is_prayer_request": False,
            "needs_deliverance": False,
            "is_urgent": False,
            "routing_suggestion": "Route to general ministry team"
        }
