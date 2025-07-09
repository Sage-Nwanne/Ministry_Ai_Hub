import uvicorn
import os
from dotenv import load_dotenv
from agents.utils import validate_environment, setup_logging

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logging()

def main():
    try:
        # Validate environment
        validate_environment()
        logger.info("Environment validated successfully")
        
        # Get host and port from environment or use defaults
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", 8000))
        
        logger.info(f"Starting Inbound Ministry Agent on {host}:{port}")
        
        # Start the FastAPI server
        uvicorn.run(
            "agents.api:app", 
            host=host, 
            port=port, 
            reload=True,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        raise

if __name__ == "__main__":
    main()