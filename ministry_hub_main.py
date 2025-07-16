"""
Ministry AI Hub - Combined Inbound & Donation System
Integrates existing inbound agents with new donation agents
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agents.api import inbound_router  # Remove 'app as inbound_app' - not used
from agents.donation_api import donation_router
from agents.utils import setup_logging, validate_environment
import uvicorn

# Setup logging
logger = setup_logging()

# Create main hub application
hub_app = FastAPI(
    title="Ministry AI Hub",
    description="Combined inbound message processing and donation engagement system",
    version="1.0.0"
)

# Add CORS middleware
hub_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
hub_app.include_router(inbound_router, prefix="/api/v1")
hub_app.include_router(donation_router, prefix="/api/v1")

@hub_app.get("/")
async def root():
    """Root endpoint for Ministry AI Hub"""
    return {
        "service": "Ministry AI Hub",
        "version": "1.0.0",
        "description": "AI-powered ministry communication hub",
        "systems": {
            "inbound": "Message processing, FAQ, escalation detection",
            "donation": "Thank you messages, impact stories, recurring giving"
        },
        "endpoints": {
            "inbound": "/api/v1/inbound",
            "donation_thank_you": "/api/v1/donation/thank-you",
            "donation_impact": "/api/v1/donation/impact-story",
            "donation_recurring": "/api/v1/donation/recurring-giving",
            "donation_qa": "/api/v1/donation/question"
        }
    }

@hub_app.get("/health")
async def health_check():
    """Comprehensive health check"""
    try:
        # Validate environment
        validate_environment()
        
        return {
            "status": "healthy",
            "systems": {
                "inbound_agents": "operational",
                "donation_agents": "operational",
                "environment": "validated"
            }
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")

if __name__ == "__main__":
    logger.info("Starting Ministry AI Hub...")
    
    try:
        validate_environment()
        logger.info("Environment validation passed")
    except Exception as e:
        logger.warning(f"Environment validation warning: {str(e)}")
    
    uvicorn.run(
        "ministry_hub_main:hub_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
