from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from agents.inbound.inbound_agent import inbound_agent
from agents.inbound.swarm_agents import (
    detect_escalation_swarm,
    translate_message_swarm,
    route_prayer_request_swarm
)
from agents.shared.analytics import log_interaction
from agents.shared.utils import setup_logging
from agents.shared.faq_tool import get_answer
import time

# Setup logging
logger = setup_logging()

# Create router for inbound system
inbound_router = APIRouter(prefix="/inbound", tags=["Inbound Communications"])

class MessageRequest(BaseModel):
    message: str
    user_id: str = "anonymous"
    source: str = "website"
    language: str = "en"  # 🆕 Language support

class TranslationRequest(BaseModel):
    message: str
    target_language: str
    
class PrayerRequest(BaseModel):
    message: str
    user_id: str = "anonymous"
    urgency: str = "normal"  # normal, urgent, emergency

def process_and_log(user_id: str, message: str, response: str, 
                   needs_escalation: bool, faq_matched: bool, 
                   response_time_ms: float, source: str, language: str):
    """Background task to log interactions"""
    logger.info(f"User {user_id} ({language}): {message[:100]}...")
    logger.info(f"Response: {response[:100]}...")
    logger.info(f"Escalation: {needs_escalation}, FAQ matched: {faq_matched}")
    
    try:
        log_interaction(
            user_id=user_id,
            message_type=source,
            response_time_ms=response_time_ms,
            escalated=needs_escalation,
            faq_matched=faq_matched,
            language=language
        )
    except Exception as e:
        logger.error(f"Failed to log analytics: {str(e)}")

@inbound_router.get("/")
async def inbound_health():
    return {
        "status": "healthy", 
        "service": "inbound_communications",
        "features": ["escalation_detection", "faq_processing", "multilingual", "prayer_routing"]
    }

@inbound_router.post("/process")
async def process_message(req: MessageRequest, background_tasks: BackgroundTasks):
    """Process inbound ministry message with multilingual support"""
    if not req.message or req.message.strip() == "":
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    start_time = time.time()
    
    try:
        # Process the message
        response, faq_matched, needs_escalation = inbound_agent(req.message, req.language)
        
        # Calculate response time
        response_time_ms = (time.time() - start_time) * 1000
        
        # Log the interaction in the background
        background_tasks.add_task(
            process_and_log, 
            req.user_id, 
            req.message, 
            response, 
            needs_escalation,
            faq_matched,
            response_time_ms,
            req.source,
            req.language
        )
        
        return {
            "response": response,
            "needs_escalation": needs_escalation,
            "faq_matched": faq_matched,
            "language": req.language,
            "response_time_ms": response_time_ms
        }
    except Exception as e:
        logger.error(f"Error processing inbound message: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process message")

@inbound_router.post("/translate")
async def translate_message(req: TranslationRequest):
    """🆕 Translate message to target language"""
    try:
        translated = translate_message_swarm(req.message, req.target_language)
        return {
            "original": req.message,
            "translated": translated,
            "target_language": req.target_language
        }
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Translation failed")

@inbound_router.post("/prayer")
async def route_prayer(req: PrayerRequest, background_tasks: BackgroundTasks):
    """🆕 Route prayer requests and deliverance needs"""
    try:
        routing_info = route_prayer_request_swarm(req.message)
        
        # Log prayer request
        background_tasks.add_task(
            log_interaction,
            user_id=req.user_id,
            message_type="prayer_request",
            response_time_ms=0,
            escalated=routing_info["is_urgent"],
            faq_matched=False,
            language="en"
        )
        
        return {
            "message": "Prayer request received and routed",
            "routing": routing_info,
            "next_steps": "Our prayer ministry team will be in touch within 24 hours" if not routing_info["is_urgent"] else "Urgent prayer request - ministry team notified immediately"
        }
    except Exception as e:
        logger.error(f"Prayer routing error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to route prayer request")

@inbound_router.post("/faq")
async def faq_lookup(req: MessageRequest):
    """Enhanced FAQ lookup with multilingual support"""
    try:
        # Translate question to English if needed
        if req.language != "en":
            english_question = translate_message_swarm(req.message, "en")
        else:
            english_question = req.message
            
        # Get FAQ answer
        faq_answer = get_answer(english_question)
        
        if not faq_answer:
            return {"answer": None, "matched": False}
        
        # Translate answer back if needed
        if req.language != "en":
            translated_answer = translate_message_swarm(faq_answer, req.language)
        else:
            translated_answer = faq_answer
            
        return {
            "answer": translated_answer,
            "matched": True,
            "language": req.language
        }
    except Exception as e:
        logger.error(f"FAQ lookup error: {str(e)}")
        raise HTTPException(status_code=500, detail="FAQ lookup failed")