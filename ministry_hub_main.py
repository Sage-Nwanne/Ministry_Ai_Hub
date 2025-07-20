"""
Ministry AI Hub - Unified Inbound & Donation System
Professional AI-driven ministry communication platform
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agents.inbound.api import inbound_router
from agents.donation.api import donation_router
from agents.shared.utils import setup_logging, validate_environment, get_supported_languages
import uvicorn

# Setup logging
logger = setup_logging()

# Create main hub application
hub_app = FastAPI(
    title="Ministry AI Hub",
    description="Professional AI-driven ministry communication system with inbound processing and donation engagement",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
hub_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with proper prefixes
hub_app.include_router(inbound_router, prefix="/api/v1")
hub_app.include_router(donation_router, prefix="/api/v1")

@hub_app.get("/")
async def root():
    """Ministry AI Hub root endpoint"""
    return {
        "service": "Ministry AI Hub",
        "version": "2.0.0",
        "description": "Professional AI-driven ministry communication platform",
        "systems": {
            "inbound_communications": {
                "description": "Digital Minister of First Impressions",
                "features": ["message_processing", "escalation_detection", "faq_responses", "multilingual_support", "prayer_routing"]
            },
            "donation_engagement": {
                "description": "Digital Stewardship Companion", 
                "features": ["thank_you_messages", "impact_stories", "recurring_giving", "donation_qa"]
            }
        },
        "supported_languages": get_supported_languages(),
        "endpoints": {
            "inbound_process": "/api/v1/inbound/process",
            "inbound_translate": "/api/v1/inbound/translate", 
            "inbound_prayer": "/api/v1/inbound/prayer",
            "inbound_faq": "/api/v1/inbound/faq",
            "donation_thank_you": "/api/v1/donation/thank-you",
            "donation_impact": "/api/v1/donation/impact-story",
            "donation_recurring": "/api/v1/donation/recurring-giving",
            "donation_qa": "/api/v1/donation/question"
        }
    }

@hub_app.get("/health")
async def comprehensive_health_check():
    """Comprehensive health check for all systems"""
    try:
        # Validate environment
        validate_environment()
        
        health_status = {
            "status": "healthy",
            "timestamp": "2024-01-01T00:00:00Z",
            "systems": {
                "inbound_communications": {
                    "status": "operational",
                    "agents": ["escalation_detector", "scripture_recommender", "tone_polisher", "translator", "prayer_router"]
                },
                "donation_engagement": {
                    "status": "operational", 
                    "agents": ["thank_you_specialist", "impact_storyteller", "stewardship_promoter", "donation_counselor"]
                },
                "shared_services": {
                    "status": "operational",
                    "services": ["faq_system", "analytics", "logging"]
                }
            },
            "environment": "validated",
            "supported_languages": list(get_supported_languages().keys())
        }
        
        return health_status
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=503, 
            detail={
                "status": "unhealthy",
                "error": str(e),
                "systems": "degraded"
            }
        )

@hub_app.get("/info")
async def system_info():
    """Detailed system information"""
    return {
        "ministry_hub": {
            "name": "Ministry AI Hub",
            "version": "2.0.0",
            "framework": "Swarms AI",
            "api_framework": "FastAPI"
        },
        "agent_systems": {
            "inbound_communications": {
                "purpose": "Digital Minister of First Impressions",
                "capabilities": [
                    "Handle website inquiries and email questions",
                    "Offer encouragement with Dr. Myles-based messages",
                    "Route complex messages and escalate sensitive inquiries", 
                    "Answer FAQs with instant responses",
                    "Maintain authentic pastoral voice and tone",
                    "🆕 Multilingual translation support",
                    "🆕 Prayer request routing and deliverance assistance"
                ]
            },
            "donation_engagement": {
                "purpose": "Digital Stewardship Companion",
                "capabilities": [
                    "Send personalized thank-you messages with scripture-based gratitude",
                    "Share impact stories highlighting ministry achievements",
                    "Promote recurring giving and suggest donation opportunities", 
                    "Handle questions about donations and tax-related inquiries"
                ]
            }
        },
        "technical_stack": {
            "ai_framework": "Swarms",
            "language_model": "GPT-3.5-turbo",
            "api_framework": "FastAPI",
            "database": "ChromaDB (FAQ)",
            "caching": "Redis",
            "logging": "Python logging"
        }
    }

if __name__ == "__main__":
    logger.info("🚀 Starting Ministry AI Hub...")
    
    try:
        validate_environment()
        logger.info("✅ Environment validation passed")
    except Exception as e:
        logger.warning(f"⚠️ Environment validation warning: {str(e)}")
    
    uvicorn.run(
        "ministry_hub_main:hub_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
