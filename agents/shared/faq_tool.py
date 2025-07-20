import json
import os
from typing import Optional
from agents.shared.utils import setup_logging

logger = setup_logging()

def load_faq_data():
    """Load FAQ data from JSON file"""
    try:
        faq_path = os.path.join("data", "faq_data.json")
        with open(faq_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load FAQ data: {e}")
        return {"faqs": []}

def get_answer(question: str) -> Optional[str]:
    """Get FAQ answer for a question"""
    try:
        faq_data = load_faq_data()
        # Simple keyword matching - can be enhanced
        question_lower = question.lower()
        
        for faq in faq_data.get("faqs", []):
            if any(keyword in question_lower for keyword in faq.get("keywords", [])):
                return faq.get("answer")
        
        return None
    except Exception as e:
        logger.error(f"FAQ lookup failed: {e}")
        return None