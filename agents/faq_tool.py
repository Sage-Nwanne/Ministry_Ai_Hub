import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import json
import os
from agents.utils import setup_logging

logger = setup_logging()

DATA_PATH = os.getenv("FAQ_DATA_PATH", "./data/faqs.json")
COLLECTION_NAME = os.getenv("FAQ_COLLECTION", "faq")

# Load model + chroma
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    logger.info(f"ChromaDB collection '{COLLECTION_NAME}' initialized")
except Exception as e:
    logger.error(f"Failed to initialize ChromaDB: {str(e)}")
    # We'll handle this in the functions below

# Step 1: Load FAQs
def load_faqs():
    try:
        with open(DATA_PATH, "r") as f:
            faqs = json.load(f)
            logger.info(f"Loaded {len(faqs)} FAQs from {DATA_PATH}")
            return faqs
    except Exception as e:
        logger.error(f"Failed to load FAQs from {DATA_PATH}: {str(e)}")
        return []

# Step 2: Index if not already indexed
def initialize_faq_collection():
    try:
        if collection.count() == 0:
            faqs = load_faqs()
            if not faqs:
                logger.warning("No FAQs to index")
                return False
                
            for i, faq in enumerate(faqs):
                collection.add(
                    documents=[faq["question"]],
                    metadatas=[{"answer": faq["answer"]}],
                    ids=[f"faq_{i}"]
                )
            logger.info(f"Indexed {len(faqs)} FAQs in ChromaDB")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize FAQ collection: {str(e)}")
        return False

# Step 3: Retrieve best-matching answer
def get_answer(user_question: str, threshold=0.60):
    try:
        if not initialize_faq_collection():
            logger.warning("FAQ collection not initialized, returning None")
            return None
            
        result = collection.query(
            query_texts=[user_question],
            n_results=1
        )
        
        if not result["documents"] or not result["documents"][0]:
            logger.info(f"No FAQ match found for: {user_question[:50]}...")
            return None
            
        distance = result["distances"][0][0] if result["distances"] and result["distances"][0] else 1.0
        
        if distance < (1 - threshold):
            answer = result["metadatas"][0][0]["answer"]
            logger.info(f"FAQ match found (distance: {distance:.2f}): {user_question[:50]}...")
            return answer
        else:
            logger.info(f"FAQ match below threshold (distance: {distance:.2f}): {user_question[:50]}...")
            return None
            
    except Exception as e:
        logger.error(f"Error in get_faq_answer: {str(e)}")
        return None
