from agents.faq_tool import get_answer
from agents.tone_polisher import polish_response
from agents.escalation_detector import detect_escalation, get_scripture_recommendation
from agents.utils import setup_logging

# Setup logging
logger = setup_logging()

def inbound_agent(user_message: str):
    """Process an inbound message and generate an appropriate response.
    
    Returns:
        tuple: (final_response, faq_matched)
    """
    logger.info(f"Processing message: {user_message[:100]}...")
    
    try:
        # Step 1: Check for escalation
        needs_escalation = detect_escalation(user_message)
        
        # Step 2: Get scripture recommendation
        scripture = get_scripture_recommendation(user_message)
        
        # Step 3: Get FAQ answer if available
        faq_answer = get_answer(user_message)
        faq_matched = faq_answer is not None
        
        # Step 4: Prepare response based on escalation and FAQ status
        if needs_escalation:
            logger.warning(f"ESCALATION REQUIRED for message: {user_message[:100]}...")
            raw_response = "I notice this may be a sensitive topic. While I'm here to support you spiritually, I recommend speaking with one of our pastoral staff for personalized guidance. Would you like me to have someone reach out to you?"
            context = "Sensitive topic requiring human intervention"
        elif faq_answer:
            raw_response = faq_answer
            context = "FAQ inquiry"
        else:
            raw_response = "Thank you for reaching out. Your message has been received by our ministry team."
            context = "General inquiry"
        
        # Step 5: Polish the response with Dr. Myles' tone
        final_response = polish_response(
            raw_response=raw_response,
            context=context,
            scripture=scripture
        )
        
        logger.info(f"Generated response: {final_response[:100]}...")
        return final_response, faq_matched
    
    except Exception as e:
        logger.error(f"Error in inbound_agent: {str(e)}")
        # Provide a graceful fallback
        return "Thank you for your message. Our system is experiencing some issues, but a team member will review your message soon.", False
