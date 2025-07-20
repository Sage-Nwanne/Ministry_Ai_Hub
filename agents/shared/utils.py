import logging
import os
from typing import Optional

def setup_logging(level: str = "INFO") -> logging.Logger:
    """Setup centralized logging for all agents"""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ministry_hub.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("MinistryHub")

def validate_environment() -> bool:
    """Validate required environment variables"""
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return True

def get_supported_languages() -> dict:
    """Get list of supported languages"""
    return {
        "en": "English",
        "es": "Spanish", 
        "fr": "French",
        "pt": "Portuguese",
        "de": "German"
    }