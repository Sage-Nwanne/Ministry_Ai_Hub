import csv
import os
import time
from datetime import datetime
from agents.utils import setup_logging

logger = setup_logging()

# Get analytics file path from environment or use default
ANALYTICS_FILE = os.getenv("ANALYTICS_FILE", "logs/analytics.csv")

# Ensure logs directory exists
os.makedirs(os.path.dirname(ANALYTICS_FILE), exist_ok=True)

# Create CSV file with headers if it doesn't exist
if not os.path.exists(ANALYTICS_FILE):
    with open(ANALYTICS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'user_id', 'message_type', 
                         'response_time_ms', 'escalated', 'faq_matched'])

def log_interaction(user_id, message_type, response_time_ms, 
                   escalated=False, faq_matched=False):
    """Log an interaction to the analytics CSV file"""
    try:
        with open(ANALYTICS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                user_id,
                message_type,
                response_time_ms,
                escalated,
                faq_matched
            ])
        logger.info(f"Analytics logged for user {user_id}")
    except Exception as e:
        logger.error(f"Failed to log analytics: {str(e)}")
        raise

def get_analytics_summary():
    """Return basic analytics summary"""
    if not os.path.exists(ANALYTICS_FILE):
        return {"error": "No analytics data available"}
    
    try:
        total_messages = 0
        escalated_count = 0
        faq_matched_count = 0
        avg_response_time = 0
        message_types = {}
        
        with open(ANALYTICS_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            response_times = []
            
            for row in reader:
                total_messages += 1
                
                # Count escalations
                if row.get('escalated', '').lower() == 'true':
                    escalated_count += 1
                
                # Count FAQ matches
                if row.get('faq_matched', '').lower() == 'true':
                    faq_matched_count += 1
                
                # Track message types
                msg_type = row.get('message_type', 'unknown')
                message_types[msg_type] = message_types.get(msg_type, 0) + 1
                
                # Track response times
                try:
                    response_times.append(float(row.get('response_time_ms', 0)))
                except (ValueError, TypeError):
                    pass
        
        if response_times:
            avg_response_time = sum(response_times) / len(response_times)
        
        return {
            "total_messages": total_messages,
            "escalated_count": escalated_count,
            "escalation_rate": escalated_count / total_messages if total_messages else 0,
            "faq_matched_count": faq_matched_count,
            "faq_rate": faq_matched_count / total_messages if total_messages else 0,
            "avg_response_time_ms": avg_response_time,
            "message_types": message_types
        }
    except Exception as e:
        logger.error(f"Failed to generate analytics summary: {str(e)}")
        raise
