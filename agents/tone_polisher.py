import os
import hashlib
import time
import requests
from dotenv import load_dotenv
from agents.escalation_detector import get_random_scripture
from agents.utils import setup_logging, get_redis_client

logger = setup_logging()
redis_client = get_redis_client()

load_dotenv()

# LM Studio endpoint
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1/chat/completions")
MODEL_NAME = os.getenv("LM_MODEL_NAME", "mythomax-13b")

# Prompt template
TONE_PROMPT = """
You are Dr. Myles, a compassionate and wise spiritual leader...

Context: {context}
Scripture: {scripture}

Original:
\"\"\"{raw_response}\"\"\"

Rewrite this as Dr. Myles would say it. Be pastoral, encouraging, and incorporate the scripture naturally if provided.
"""

# Generate cache key
def hash_prompt(prompt: str) -> str:
    return "tone:" + hashlib.sha256(prompt.encode()).hexdigest()

# Main tone polishing function
def polish_response(raw_response, context="", scripture=""):
    # If no scripture provided, get a random one
    if not scripture or scripture.strip() == "":
        scripture = get_random_scripture()
        logger.info(f"Using random scripture: {scripture}")
    
    prompt = TONE_PROMPT.format(
        raw_response=raw_response,
        context=context,
        scripture=scripture
    )
    key = hash_prompt(prompt)

    try:
        cached = redis_client.get(key)
        if cached:
            logger.info("Using cached tone-polished response")
            return cached

        payload = {
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500
        }

        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                response = requests.post(LM_STUDIO_URL, json=payload, timeout=10)
                response.raise_for_status()
                result = response.json()
                polished = result["choices"][0]["message"]["content"].strip()

                redis_client.setex(key, 86400, polished)
                return polished

            except Exception as e:
                logger.error(f"Local API error (attempt {attempt+1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (2 ** attempt))
                else:
                    raise
    except Exception as e:
        logger.error(f"Failed to polish response: {str(e)}")
        # Fallback if all retries fail
        if scripture:
            fallback = f"Beloved, {raw_response} As the scripture says in {scripture}, we must trust in the Lord with all our heart."
        else:
            fallback = f"Beloved, {raw_response} Stay blessed and keep the faith."
        logger.warning(f"Using fallback response: {fallback[:50]}...")
        return fallback
