from swarms import Agent
from swarms.models import OpenAIChat
import os
import json
from dotenv import load_dotenv
from agents.utils import setup_logging

load_dotenv()
logger = setup_logging()

# Initialize OpenAI model for donation agents
def initialize_donation_model():
    """Initialize OpenAI model for donation agents"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("OPENAI_API_KEY not found for donation agents")
        return None
    
    try:
        model = OpenAIChat(
            openai_api_key=api_key,
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=400
        )
        return model
    except Exception as e:
        logger.error(f"Failed to initialize donation model: {str(e)}")
        return None

model = initialize_donation_model()

def load_impact_stories():
    """Load impact stories data"""
    try:
        with open('./data/impact_stories.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load impact stories: {str(e)}")
        return []

def load_verses_for_giving():
    """Load verses related to giving and generosity"""
    try:
        with open('./data/verses.json', 'r') as f:
            verses = json.load(f)
            # Filter for giving-related verses
            giving_verses = [v for v in verses if any(topic in v.get('text', '').lower() 
                           for topic in ['give', 'generous', 'cheerful', 'blessing'])]
            return giving_verses[:5]  # Return top 5
    except Exception as e:
        logger.error(f"Failed to load verses: {str(e)}")
        return []

# Thank You Agent
thank_you_agent = Agent(
    agent_name="ThankYouAgent",
    system_prompt=f"""You are a grateful ministry leader writing personalized thank-you notes.
    
    Create warm, heartfelt thank-you messages that:
    - Express genuine gratitude for the donor's generosity
    - Include relevant scripture about giving or blessing
    - Mention the specific impact their gift will have
    - Maintain a pastoral, encouraging tone
    
    Available verses: {load_verses_for_giving()}
    
    Format: Write a complete thank-you message ready to send.""",
    llm=model,
    max_loops=1,
    verbose=False
) if model else None

# Impact Story Agent
impact_story_agent = Agent(
    agent_name="ImpactStoryAgent",
    system_prompt=f"""You are a ministry storyteller who shares compelling impact narratives.
    
    Transform impact data into engaging stories that:
    - Highlight specific ministry achievements
    - Show tangible results from donor support
    - Include emotional connection and spiritual significance
    - Encourage continued partnership
    
    Available impact stories: {load_impact_stories()}
    
    Create short, compelling narratives that inspire and inform supporters.""",
    llm=model,
    max_loops=1,
    verbose=False
) if model else None

# Recurring Giving Agent
recurring_giving_agent = Agent(
    agent_name="RecurringGivingAgent",
    system_prompt="""You are a gentle stewardship counselor promoting recurring giving.
    
    Create encouraging messages about recurring donations that:
    - Emphasize the spiritual discipline of regular giving
    - Show the sustained impact of consistent support
    - Include relevant scripture about faithfulness and stewardship
    - Suggest practical giving amounts and frequencies
    - Never pressure, always encourage with grace
    
    Focus on the joy and blessing of partnership in ministry.""",
    llm=model,
    max_loops=1,
    verbose=False
) if model else None

# Donation Q&A Agent
donation_qa_agent = Agent(
    agent_name="DonationQAAgent",
    system_prompt="""You are a knowledgeable ministry administrator answering donation questions.
    
    Provide clear, helpful answers about:
    - Tax deductibility and receipt processes
    - Donation methods and security
    - Recurring giving setup and changes
    - Ministry fund allocation and transparency
    - Biblical perspectives on giving
    
    Always be accurate, transparent, and include relevant scripture when appropriate.
    If you don't know specific policy details, direct them to contact the ministry office.""",
    llm=model,
    max_loops=1,
    verbose=False
) if model else None

# Donation workflow functions
def send_thank_you_message(donor_name: str, amount: str) -> str:
    """Generate personalized thank you message"""
    if not thank_you_agent:
        return f"Thank you {donor_name} for your generous gift of {amount}!"
    
    try:
        prompt = f"Write a thank you message for {donor_name} who donated {amount}"
        result = thank_you_agent.run(prompt)
        logger.info(f"Generated thank you for {donor_name}")
        return str(result)
    except Exception as e:
        logger.error(f"Thank you generation error: {str(e)}")
        return f"Thank you {donor_name} for your generous gift of {amount}!"

def share_impact_story(category: str = None) -> str:
    """Share relevant impact story"""
    if not impact_story_agent:
        return "Your donations are making a real difference in our community!"
    
    try:
        stories = load_impact_stories()
        if category:
            filtered_stories = [s for s in stories if s.get('category') == category]
            stories = filtered_stories if filtered_stories else stories
        
        prompt = f"Create an impact story based on: {stories[:2]}"
        result = impact_story_agent.run(prompt)
        logger.info(f"Generated impact story for category: {category}")
        return str(result)
    except Exception as e:
        logger.error(f"Impact story generation error: {str(e)}")
        return "Your donations are making a real difference in our community!"

def promote_recurring_giving(donor_name: str = None) -> str:
    """Promote recurring giving"""
    if not recurring_giving_agent:
        return "Consider setting up recurring giving to support our ongoing ministry!"
    
    try:
        prompt = f"Encourage recurring giving for {donor_name or 'supporter'}"
        result = recurring_giving_agent.run(prompt)
        logger.info(f"Generated recurring giving message")
        return str(result)
    except Exception as e:
        logger.error(f"Recurring giving promotion error: {str(e)}")
        return "Consider setting up recurring giving to support our ongoing ministry!"

def answer_donation_question(question: str) -> str:
    """Answer donation-related questions"""
    if not donation_qa_agent:
        return "Please contact our ministry office for donation questions."
    
    try:
        result = donation_qa_agent.run(question)
        logger.info(f"Answered donation question: {question[:50]}...")
        return str(result)
    except Exception as e:
        logger.error(f"Donation Q&A error: {str(e)}")
        return "Please contact our ministry office for donation questions."

# Export functions
__all__ = [
    'thank_you_agent',
    'impact_story_agent', 
    'recurring_giving_agent',
    'donation_qa_agent',
    'send_thank_you_message',
    'share_impact_story',
    'promote_recurring_giving',
    'answer_donation_question'
]