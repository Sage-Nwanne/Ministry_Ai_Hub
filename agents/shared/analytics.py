import time
from typing import Dict, Any
from agents.shared.utils import setup_logging

logger = setup_logging()

def log_interaction(user_id: str, message_type: str, response_time_ms: float, 
                   escalated: bool = False, faq_matched: bool = False, **kwargs):
    """Log interaction analytics"""
    try:
        log_data = {
            "timestamp": time.time(),
            "user_id": user_id,
            "message_type": message_type,
            "response_time_ms": response_time_ms,
            "escalated": escalated,
            "faq_matched": faq_matched,
            **kwargs
        }
        logger.info(f"Analytics: {log_data}")
    except Exception as e:
        logger.error(f"Analytics logging failed: {e}")

def get_analytics_summary() -> Dict[str, Any]:
    """Get analytics summary"""
    return {
        "status": "analytics_active",
        "metrics": "logged_to_system"
    }