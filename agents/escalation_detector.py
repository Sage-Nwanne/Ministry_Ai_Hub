import os
import hashlib
import json
import random
import openai
from dotenv import load_dotenv
from agents.utils import setup_logging, get_redis_client

# Setup logging
logger = setup_logging()
redis_client = get_redis_client()

load_dotenv()

ESCALATION_PROMPT = """
Analyze the following message and determine if it contains sensitive topics that require human intervention.
Sensitive topics include: suicidal thoughts, severe depression, abuse, violence, self-harm, or urgent medical needs.

Message: {message}

Return only "ESCALATE" if this needs human attention, or "NORMAL" if it can be handled automatically.
"""

SCRIPTURE_PROMPT = """
Based on the following message, suggest an appropriate scripture verse that would provide comfort, guidance, or wisdom.
Keep your response brief - just the scripture reference and verse.

Message: {message}
"""

# Load verses for fallback
def load_verses():
    try:
        with open("data/verses.json", "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load verses.json: {str(e)}")
        return [
            {
                "reference": "Proverbs 3:5-6",
                "text": "Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths."
            },
            {
                "reference": "Psalm 23:1",
                "text": "The Lord is my shepherd; I shall not want."
            },
            {
                "reference": "Isaiah 41:10",
                "text": "Fear not, for I am with you; be not dismayed, for I am your God."
            }
        ]

VERSES = load_verses()

def get_random_scripture():
    """Get a random scripture from the verses list"""
    verse = random.choice(VERSES)
    return f"{verse['reference']} - {verse['text']}"

def detect_escalation(message: str) -> bool:
    """Detect if a message contains sensitive topics requiring escalation."""
    prompt = ESCALATION_PROMPT.format(message=message)
    key = "escalation:" + hashlib.sha256(prompt.encode()).hexdigest()

    try:
        cached = redis_client.get(key)
        if cached:
            return cached.decode("utf-8") == "ESCALATE"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=10
        )
        result = response["choices"][0]["message"]["content"].strip()
        redis_client.setex(key, 86400, result)
        logger.info(f"Escalation detection for message: {message[:50]}... Result: {result}")
        return "ESCALATE" in result
    except Exception as e:
        logger.error(f"Escalation detection error: {str(e)}")
        return True  # default to escalate if unsure

def get_scripture_recommendation(message: str) -> str:
    """Get a scripture recommendation based on the message content."""
    prompt = SCRIPTURE_PROMPT.format(message=message)
    key = "scripture:" + hashlib.sha256(prompt.encode()).hexdigest()

    try:
        cached = redis_client.get(key)
        if cached:
            return cached.decode("utf-8")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        scripture = response["choices"][0]["message"]["content"].strip()
        redis_client.setex(key, 86400, scripture)
        logger.info(f"Scripture recommendation for message: {message[:50]}... Scripture: {scripture}")
        return scripture
    except Exception as e:
        logger.error(f"Scripture recommendation error: {str(e)}")
        return get_random_scripture()
