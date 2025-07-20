from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.donation.donation_agents import (
    generate_thank_you_message,
    generate_impact_story,
    promote_recurring_giving,
    answer_donation_question
)
from agents.shared.utils import setup_logging

logger = setup_logging()

donation_router = APIRouter(prefix="/donation", tags=["Donation Engagement"])

class ThankYouRequest(BaseModel):
    donor_name: str
    amount: str
    email: str = ""

class ImpactStoryRequest(BaseModel):
    category: str = "general"
    donor_segment: str = "regular_donor"

class RecurringGivingRequest(BaseModel):
    donor_name: str
    current_amount: str = ""
    suggested_frequency: str = "monthly"

class DonationQARequest(BaseModel):
    question: str
    donor_context: str = "general"

@donation_router.get("/")
async def donation_health():
    return {"status": "healthy", "service": "donation_engagement"}

@donation_router.post("/thank-you")
async def create_thank_you(req: ThankYouRequest):
    try:
        message = generate_thank_you_message(req.donor_name, req.amount, req.email)
        return {"thank_you_message": message}
    except Exception as e:
        logger.error(f"Thank you generation failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate thank you message")

@donation_router.post("/impact-story")
async def create_impact_story(req: ImpactStoryRequest):
    try:
        story = generate_impact_story(req.category, req.donor_segment)
        return {"impact_story": story}
    except Exception as e:
        logger.error(f"Impact story generation failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate impact story")

@donation_router.post("/recurring")
async def promote_recurring(req: RecurringGivingRequest):
    try:
        message = promote_recurring_giving(req.donor_name, req.current_amount)
        return {"recurring_message": message}
    except Exception as e:
        logger.error(f"Recurring giving promotion failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate recurring giving message")

@donation_router.post("/qa")
async def donation_qa(req: DonationQARequest):
    try:
        answer = answer_donation_question(req.question, req.donor_context)
        return {"answer": answer}
    except Exception as e:
        logger.error(f"Donation Q&A failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to answer donation question")
