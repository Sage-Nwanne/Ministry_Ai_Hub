from swarms.structs import SequentialWorkflow
from agents.swarm_agents import (
    escalation_agent,
    scripture_agent, 
    tone_agent
)
from agents.utils import setup_logging

logger = setup_logging()

# Create a sequential workflow for complete message processing
ministry_workflow = SequentialWorkflow(
    agents=[escalation_agent, scripture_agent, tone_agent],
    max_loops=1,
    verbose=True,
)

def process_message_workflow(message: str, faq_answer: str = None):
    """Process a message through the complete Swarms workflow"""
    try:
        # Prepare workflow input
        if faq_answer:
            workflow_input = f"""
            User Message: {message}
            FAQ Answer Available: {faq_answer}
            
            1. First, check if this message needs escalation
            2. Then, recommend appropriate scripture
            3. Finally, polish the response in Dr. Myles' pastoral tone
            """
        else:
            workflow_input = f"""
            User Message: {message}
            
            1. First, check if this message needs escalation  
            2. Then, recommend appropriate scripture
            3. Finally, create and polish a pastoral response
            """
        
        # Run the workflow
        result = ministry_workflow.run(workflow_input)
        logger.info(f"Swarms workflow completed for: {message[:50]}...")
        return str(result)
        
    except Exception as e:
        logger.error(f"Swarms workflow error: {str(e)}")
        return "Thank you for your message. A team member will respond soon."

def get_workflow_status():
    """Get the current status of the workflow"""
    return {
        "agents": len(ministry_workflow.agents),
        "workflow_type": "sequential",
        "framework": "swarms"
    }
