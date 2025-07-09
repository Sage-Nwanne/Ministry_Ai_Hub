from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from pydantic import BaseModel
from agents.tone_polisher import polish_response
from agents.inbound_agent import inbound_agent
from agents.escalation_detector import detect_escalation
from agents.analytics import log_interaction, get_analytics_summary
from agents.utils import setup_logging, validate_environment
from agents.faq_tool import get_answer
import time

# Setup logging
logger = setup_logging()

# Validate environment variables on startup
try:
    validate_environment()
except EnvironmentError as e:
    logger.error(f"Environment validation failed: {str(e)}")
    # We'll continue but log the error

app = FastAPI(
    title="Inbound Ministry Agent",
    description="API for processing inbound ministry messages with AI assistance",
    version="1.0.0"
)

class ToneRequest(BaseModel):
    raw_response: str
    context: str = ""
    scripture: str = ""

class MessageRequest(BaseModel):
    message: str
    user_id: str = "anonymous"
    source: str = "website"  # website, email, chat, form

def process_and_log(user_id: str, message: str, response: str, 
                   needs_escalation: bool, faq_matched: bool, 
                   response_time_ms: float, source: str):
    """Background task to log interactions"""
    logger.info(f"User {user_id}: {message[:100]}...")
    logger.info(f"Response: {response[:100]}...")
    logger.info(f"Escalation: {needs_escalation}, FAQ matched: {faq_matched}")
    
    # Log to analytics
    try:
        log_interaction(
            user_id=user_id,
            message_type=source,
            response_time_ms=response_time_ms,
            escalated=needs_escalation,
            faq_matched=faq_matched
        )
    except Exception as e:
        logger.error(f"Failed to log analytics: {str(e)}")

@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "ministry_bot"}

@app.post("/polish")
async def polish(req: ToneRequest):
    try:
        return {
            "dr_myles_response": polish_response(
                req.raw_response,
                req.context,
                req.scripture
            )
        }
    except Exception as e:
        logger.error(f"Error in polish endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to polish response")

@app.post("/inbound")
async def inbound(req: MessageRequest, background_tasks: BackgroundTasks):
    if not req.message or req.message.strip() == "":
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    # Start timing
    start_time = time.time()
    
    try:
        # Process the message
        response, faq_matched = inbound_agent(req.message)
        
        # Check for escalation separately to include in response
        needs_escalation = detect_escalation(req.message)
        
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
            req.source
        )
        
        return {
            "reply": response,
            "needs_escalation": needs_escalation
        }
    except Exception as e:
        logger.error(f"Error processing inbound message: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process message")

@app.get("/analytics")
async def analytics():
    try:
        return get_analytics_summary()
    except Exception as e:
        logger.error(f"Error retrieving analytics: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve analytics")

class FAQRequest(BaseModel):
    question: str

@app.post("/faq")
async def faq(req: FAQRequest, background_tasks: BackgroundTasks):
    if not req.question or req.question.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        answer = get_answer(req.question)
        
        # Optional: Log FAQ match for analytics
        background_tasks.add_task(
            process_and_log,
            user_id="anonymous",  # or adapt as needed
            message=req.question,
            response=answer,
            needs_escalation=False,
            faq_matched=True,
            response_time_ms=0,
            source="faq"
        )
        
        return {"answer": answer}
    except Exception as e:
        logger.error(f"Error answering FAQ: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch answer")
    
@app.post("/escalation-check")
async def escalation_check(req: MessageRequest):
    try:
        escalate = detect_escalation(req.message)
        return {"should_escalate": escalate}
    except Exception as e:
        logger.error(f"Escalation check failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Escalation check failed")
