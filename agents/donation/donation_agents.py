from swarms import Agent
from swarms.utils.litellm_wrapper import LiteLLM  # Updated import
from agents.shared.utils import setup_logging
import os
import json
import random

logger = setup_logging()

# Initialize the language model with LM Studio configuration
model = LiteLLM(
    model_name="openai/qwen3-4b:2",  # Add openai/ prefix
    api_base=os.getenv("LM_STUDIO_API_BASE", "http://192.168.1.88:1234/v1"),
    api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    temperature=0.1,
    custom_llm_provider="openai",  # Specify provider
)

# Thank You Agent
thank_you_agent = Agent(
    agent_name="DonorThankYouSpecialist",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are Dr. Myles' donation appreciation specialist. 
    Create heartfelt, personalized thank-you messages that:
    - Express genuine gratitude
    - Include relevant scripture about giving
    - Maintain Dr. Myles' warm, pastoral tone
    - Encourage continued partnership
    
    Keep messages personal but professional, around 150-200 words.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Impact Story Agent
impact_story_agent = Agent(
    agent_name="MinistryImpactStoryteller",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are a ministry impact storyteller for Dr. Myles' organization.
    Create compelling stories that show how donations make a difference:
    - Use real ministry categories (youth, seniors, outreach, missions)
    - Include specific but realistic metrics
    - Maintain inspirational and hopeful tone
    - Connect giving to kingdom impact
    
    Stories should be 200-300 words and emotionally engaging.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Recurring Giving Agent
recurring_giving_agent = Agent(
    agent_name="StewardshipPromoter",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are a biblical stewardship counselor for Dr. Myles' ministry.
    Promote recurring giving through:
    - Biblical principles of stewardship
    - Practical benefits of consistent giving
    - Personal spiritual growth through giving
    - Ministry sustainability and impact
    
    Be encouraging, not pushy. Focus on spiritual benefits.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Donation Q&A Agent
donation_qa_agent = Agent(
    agent_name="DonationCounselor",
    model_name="openai/qwen3-4b:2",  # Match LiteLLM model_name exactly
    system_prompt="""You are a donation and tax specialist for ministry giving.
    Answer questions about:
    - Tax deductibility of donations
    - Giving methods and options
    - Planned giving and legacy gifts
    - Ministry financial transparency
    
    Provide accurate, helpful information while maintaining pastoral care.""",
    llm=model,
    max_loops=1,
    verbose=False,
)

# Load impact stories data
def load_impact_stories():
    """Load impact stories from data file"""
    try:
        with open("data/impact_stories.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("Impact stories file not found, using defaults")
        return {
            "youth": [
                {
                    "title": "Youth Ministry Growth",
                    "description": "Our youth program has grown by 40% this year, reaching 150 young people weekly with mentorship and biblical teaching.",
                    "impact": "40% growth, 150 youth reached weekly"
                }
            ],
            "seniors": [
                {
                    "title": "Senior Care Ministry",
                    "description": "Monthly visits to 80 seniors in our community, providing companionship, prayer, and practical support.",
                    "impact": "80 seniors served monthly"
                }
            ]
        }

# Swarm Functions
async def send_thank_you_message(donor_name: str, amount: str, email: str = None) -> dict:
    """Generate personalized thank you message"""
    try:
        prompt = f"""
        Create a heartfelt thank-you message for:
        Donor: {donor_name}
        Amount: {amount}
        
        Include appropriate scripture and express genuine gratitude in Dr. Myles' pastoral voice.
        """
        
        result = thank_you_agent.run(prompt)
        
        return {
            "message": str(result),
            "donor_name": donor_name,
            "amount": amount,
            "email": email
        }
    except Exception as e:
        logger.error(f"Thank you generation failed: {e}")
        return {
            "message": f"Dear {donor_name}, thank you for your generous gift of {amount}. Your support makes a tremendous difference in our ministry.",
            "donor_name": donor_name,
            "amount": amount,
            "email": email
        }

async def share_impact_story(category: str = "general", donor_segment: str = "regular") -> dict:
    """Generate ministry impact story"""
    try:
        impact_data = load_impact_stories()
        
        # Get relevant story data
        if category in impact_data:
            story_data = random.choice(impact_data[category])
        else:
            story_data = random.choice(impact_data.get("general", [{"title": "Ministry Impact", "description": "Your support continues to transform lives in our community."}]))
        
        prompt = f"""
        Create an inspiring impact story based on:
        Category: {category}
        Donor Segment: {donor_segment}
        Story Data: {story_data}
        
        Make it compelling and show how donations create real kingdom impact.
        """
        
        result = impact_story_agent.run(prompt)
        
        return {
            "story": str(result),
            "category": category,
            "donor_segment": donor_segment
        }
    except Exception as e:
        logger.error(f"Impact story generation failed: {e}")
        return {
            "story": "Your generous support continues to transform lives and advance God's kingdom through our ministry work.",
            "category": category,
            "donor_segment": donor_segment
        }

async def promote_recurring_giving(donor_name: str, current_amount: str = None) -> dict:
    """Promote recurring giving with biblical stewardship"""
    try:
        prompt = f"""
        Create a message promoting recurring giving for:
        Donor: {donor_name}
        Current Gift: {current_amount if current_amount else "Not specified"}
        
        Focus on biblical stewardship principles and spiritual benefits of consistent giving.
        """
        
        result = recurring_giving_agent.run(prompt)
        
        return {
            "message": str(result),
            "donor_name": donor_name,
            "current_amount": current_amount
        }
    except Exception as e:
        logger.error(f"Recurring giving promotion failed: {e}")
        return {
            "message": f"Dear {donor_name}, consider the blessing of consistent giving as an act of worship and partnership in ministry.",
            "donor_name": donor_name,
            "current_amount": current_amount
        }

async def answer_donation_question(question: str, donor_context: str = "general") -> dict:
    """Answer donation and tax-related questions"""
    try:
        prompt = f"""
        Answer this donation question:
        Question: {question}
        Donor Context: {donor_context}
        
        Provide accurate, helpful information while maintaining pastoral care.
        """
        
        result = donation_qa_agent.run(prompt)
        
        return {
            "answer": str(result),
            "question": question,
            "donor_context": donor_context
        }
    except Exception as e:
        logger.error(f"Donation Q&A failed: {e}")
        return {
            "answer": "Thank you for your question. Our ministry team will provide you with detailed information about donation policies and tax benefits.",
            "question": question,
            "donor_context": donor_context
        }

# Add these SYNC wrapper functions that your API expects
def generate_thank_you_message(donor_name: str, amount: str, email: str = "") -> str:
    """Generate personalized thank you message (sync wrapper)"""
    try:
        prompt = f"""
        Create a heartfelt thank-you message for:
        Donor: {donor_name}
        Amount: {amount}
        
        Include appropriate scripture and express genuine gratitude in Dr. Myles' pastoral voice.
        """
        result = thank_you_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Thank you generation failed: {e}")
        return f"Dear {donor_name}, thank you for your generous gift of {amount}. Your support makes a tremendous difference in our ministry."

def generate_impact_story(category: str = "general", donor_segment: str = "regular") -> str:
    """Generate ministry impact story (sync wrapper)"""
    try:
        prompt = f"""
        Create an inspiring impact story for:
        Category: {category}
        Donor Segment: {donor_segment}
        
        Make it compelling and show how donations create real kingdom impact.
        """
        result = impact_story_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Impact story generation failed: {e}")
        return "Your generous support continues to transform lives and advance God's kingdom through our ministry work."

def promote_recurring_giving(donor_name: str, current_amount: str = None) -> str:
    """Promote recurring giving (sync wrapper)"""
    try:
        prompt = f"""
        Create a message promoting recurring giving for:
        Donor: {donor_name}
        Current Gift: {current_amount if current_amount else "Not specified"}
        
        Focus on biblical stewardship principles and spiritual benefits.
        """
        result = recurring_giving_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Recurring giving promotion failed: {e}")
        return f"Dear {donor_name}, consider making your giving a regular spiritual discipline through recurring donations."

def answer_donation_question(question: str, donor_context: str = "general") -> str:
    """Answer donation questions (sync wrapper)"""
    try:
        prompt = f"""
        Answer this donation question:
        Question: {question}
        Donor Context: {donor_context}
        
        Provide accurate, helpful information with pastoral care.
        """
        result = donation_qa_agent.run(prompt)
        return str(result)
    except Exception as e:
        logger.error(f"Donation Q&A failed: {e}")
        return "Thank you for your question. Our ministry team will provide detailed information about donation policies."

def load_impact_stories():
    """Load impact stories from JSON file"""
    try:
        import json
        import os
        story_path = os.path.join("data", "impact_stories.json")
        with open(story_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load impact stories: {e}")
        return {
            "general": [{"title": "Ministry Impact", "description": "Your support transforms lives"}],
            "youth": [{"title": "Youth Ministry", "description": "Reaching the next generation"}],
            "seniors": [{"title": "Senior Ministry", "description": "Caring for our elders"}]
        }
