from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
from agents.donation_agents import (
    send_thank_you_message,
    share_impact_story, 
    promote_recurring_giving,
    answer_donation_question
)
from agents.utils import setup_logging
import time

logger = setup_logging()

# Create donation router
donation_router = APIRouter(prefix="/donation", tags=["donation"])

# Request models
class ThankYouRequest(BaseModel):
    donor_name: str
    amount: str
    email: Optional[str] = None

class ImpactStoryRequest(BaseModel):
    category: Optional[str] = None
    donor_segment: Optional[str] = None

class RecurringGivingRequest(BaseModel):
    donor_name: Optional[str] = None
    current_amount: Optional[str] = None

class DonationQuestionRequest(BaseModel):
    question: str
    donor_context: Optional[str] = None

@donation_router.post("/thank-you")
async def generate_thank_you(req: ThankYouRequest, background_tasks: BackgroundTasks):
    """Generate personalized thank you message"""
    start_time = time.time()
    
    try:
        message = send_thank_you_message(req.donor_name, req.amount)
        
        response_time = (time.time() - start_time) * 1000
        logger.info(f"Thank you generated in {response_time:.2f}ms")
        
        return {
            "message": message,
            "donor_name": req.donor_name,
            "amount": req.amount,
            "response_time_ms": response_time
        }
    except Exception as e:
        logger.error(f"Thank you generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate thank you message")

@donation_router.post("/impact-story")
async def get_impact_story(req: ImpactStoryRequest):
    """Get relevant impact story"""
    start_time = time.time()
    
    try:
        story = share_impact_story(req.category)
        
        response_time = (time.time() - start_time) * 1000
        logger.info(f"Impact story generated in {response_time:.2f}ms")
        
        return {
            "story": story,
            "category": req.category,
            "response_time_ms": response_time
        }
    except Exception as e:
        logger.error(f"Impact story generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate impact story")

@donation_router.post("/recurring-giving")
async def promote_recurring(req: RecurringGivingRequest):
    """Promote recurring giving"""
    start_time = time.time()
    
    try:
        message = promote_recurring_giving(req.donor_name)
        
        response_time = (time.time() - start_time) * 1000
        logger.info(f"Recurring giving message generated in {response_time:.2f}ms")
        
        return {
            "message": message,
            "donor_name": req.donor_name,
            "response_time_ms": response_time
        }
    except Exception as e:
        logger.error(f"Recurring giving promotion failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate recurring giving message")

@donation_router.post("/question")
async def answer_question(req: DonationQuestionRequest):
    """Answer donation-related questions"""
    start_time = time.time()
    
    try:
        answer = answer_donation_question(req.question)
        
        response_time = (time.time() - start_time) * 1000
        logger.info(f"Donation question answered in {response_time:.2f}ms")
        
        return {
            "question": req.question,
            "answer": answer,
            "response_time_ms": response_time
        }
    except Exception as e:
        logger.error(f"Donation Q&A failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to answer donation question")

@donation_router.get("/health")
async def donation_health():
    """Health check for donation system"""
    return {
        "status": "healthy",
        "service": "donation_agents",
        "endpoints": [
            "/donation/thank-you",
            "/donation/impact-story", 
            "/donation/recurring-giving",
            "/donation/question"
        ]
    }