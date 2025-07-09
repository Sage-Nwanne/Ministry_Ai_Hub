import os
import redis
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "ministry_bot.log")
    
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        numeric_level = logging.INFO
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file
    )
    return logging.getLogger('ministry_bot')

# Redis connection singleton
_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0,
            decode_responses=True
        )
    return _redis_client

# Environment validation
def validate_environment():
    required_vars = [
        "REDIS_HOST",
        "REDIS_PORT",
        "LM_STUDIO_URL",
        "LM_MODEL_NAME",
        "OPENAI_API_KEY"
    ]
    
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")