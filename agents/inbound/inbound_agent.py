from agents.inbound.swarm_agents import (
    detect_escalation_swarm, 
    get_scripture_recommendation_swarm, 
    polish_response_swarm,
    process_faq_response_swarm,
    translate_message_swarm,
    route_prayer_request_swarm
)
from agents.shared.faq_tool import get_answer
from agents.shared.utils import setup_logging

# Setup logging
logger = setup_logging()

def inbound_agent(user_message: str, user_language: str = "en"):
    """Process an inbound message using optimized agent routing.
    
    Args:
        user_message: The incoming message
        user_language: Language code (en, es, fr, etc.)
    
    Returns:
        tuple: (final_response, faq_matched, needs_escalation)
    """
    logger.info(f"Processing message with optimized routing: {user_message[:100]}...")
    
    try:
        # Step 1: Translate to English if needed
        if user_language != "en":
            translated_message = translate_message_swarm(user_message, "en")
        else:
            translated_message = user_message
        
        # Step 2: ALWAYS check for escalation first (safety critical)
        needs_escalation = detect_escalation_swarm(translated_message)
        
        if needs_escalation:
            logger.warning(f"ESCALATION REQUIRED for message: {user_message[:100]}...")
            raw_response = "I notice this may be a sensitive topic. While I'm here to support you spiritually, I recommend speaking with one of our pastoral staff for personalized guidance. Would you like me to have someone reach out to you?"
            context = "Sensitive topic requiring human intervention"
            scripture = "Psalm 34:18 - The Lord is close to the brokenhearted and saves those who are crushed in spirit."
            
            # Skip other agents for escalated messages
            polished_response = polish_response_swarm(raw_response, context, scripture)
            
            if user_language != "en":
                final_response = translate_message_swarm(polished_response, user_language)
            else:
                final_response = polished_response
                
            return final_response, False, True
        
        # Step 3: Route to appropriate agent based on message type
        message_type = determine_message_type(translated_message)
        
        if message_type == "prayer_request":
            return handle_prayer_request(translated_message, user_language)
        elif message_type == "faq_inquiry":
            return handle_faq_inquiry(translated_message, user_language)
        elif message_type == "general_inquiry":
            return handle_general_inquiry(translated_message, user_language)
        else:
            return handle_default_response(translated_message, user_language)
    
    except Exception as e:
        logger.error(f"Error in optimized inbound_agent: {str(e)}")
        fallback_message = "Thank you for your message. Our system is experiencing some issues, but a team member will review your message soon."
        
        if user_language != "en":
            try:
                fallback_message = translate_message_swarm(fallback_message, user_language)
            except:
                pass
                
        return fallback_message, False, False

def determine_message_type(message: str) -> str:
    """Quickly determine message type using keyword analysis"""
    message_lower = message.lower()
    
    # Prayer request keywords
    prayer_keywords = ["pray", "prayer", "praying", "intercede", "blessing", "heal", "healing"]
    if any(keyword in message_lower for keyword in prayer_keywords):
        return "prayer_request"
    
    # FAQ keywords  
    faq_keywords = ["how", "what", "when", "where", "why", "can you", "do you", "information"]
    if any(keyword in message_lower for keyword in faq_keywords):
        return "faq_inquiry"
    
    # General inquiry
    general_keywords = ["help", "support", "guidance", "question", "need"]
    if any(keyword in message_lower for keyword in general_keywords):
        return "general_inquiry"
    
    return "default"

def handle_prayer_request(message: str, user_language: str) -> tuple:
    """Handle prayer requests efficiently"""
    logger.info("Routing to prayer request handler")
    
    # Only call relevant agents
    prayer_routing = route_prayer_request_swarm(message)
    is_prayer_request = prayer_routing.get("is_prayer_request", False)
    
    if is_prayer_request:
        raw_response = "Thank you for sharing your prayer request. I've forwarded this to our prayer ministry team, and they will be interceding for you. Would you also like to schedule a personal prayer session with one of our ministers?"
        context = "Prayer request"
        scripture = get_scripture_recommendation_swarm(message)
        
        # Polish with Dr. Myles' tone
        polished_response = polish_response_swarm(raw_response, context, scripture)
        
        # Translate if needed
        if user_language != "en":
            final_response = translate_message_swarm(polished_response, user_language)
        else:
            final_response = polished_response
            
        return final_response, False, False
    
    return handle_default_response(message, user_language)

def handle_faq_inquiry(message: str, user_language: str) -> tuple:
    """Handle FAQ inquiries efficiently"""
    logger.info("Routing to FAQ handler")
    
    # Check FAQ first
    faq_answer = get_answer(message)
    
    if faq_answer:
        # Only enhance FAQ response
        enhanced_faq = process_faq_response_swarm(faq_answer, message)
        context = "FAQ inquiry"
        
        # Get scripture and polish
        scripture = get_scripture_recommendation_swarm(message)
        polished_response = polish_response_swarm(enhanced_faq, context, scripture)
        
        if user_language != "en":
            final_response = translate_message_swarm(polished_response, user_language)
        else:
            final_response = polished_response
            
        return final_response, True, False
    
    return handle_general_inquiry(message, user_language)

def handle_general_inquiry(message: str, user_language: str) -> tuple:
    """Handle general inquiries efficiently"""
    logger.info("Routing to general inquiry handler")
    
    raw_response = "Thank you for reaching out. Your message has been received by our ministry team."
    context = "General inquiry"
    scripture = get_scripture_recommendation_swarm(message)
    
    polished_response = polish_response_swarm(raw_response, context, scripture)
    
    if user_language != "en":
        final_response = translate_message_swarm(polished_response, user_language)
    else:
        final_response = polished_response
        
    return final_response, False, False

def handle_default_response(message: str, user_language: str) -> tuple:
    """Handle default responses efficiently"""
    logger.info("Routing to default handler")
    
    raw_response = "Thank you for your message. Our ministry team will review it and respond appropriately."
    context = "Default response"
    
    polished_response = polish_response_swarm(raw_response, context, "")
    
    if user_language != "en":
        final_response = translate_message_swarm(polished_response, user_language)
    else:
        final_response = polished_response
        
    return final_response, False, False
