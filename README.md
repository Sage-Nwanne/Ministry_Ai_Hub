# Inbound Ministry Agent System

Hi Swathi,

This is the full setup and documentation for the **Inbound Ministry Agent System** I've been working on. The goal was to create a **scalable, efficient, and locally powered AI system** that can:

- ✅ Process inbound user messages
- ✅ Answer FAQs using vector search (ChromaDB)
- ✅ Tone-polish replies using a local LLM (like MythoMax) in the voice of “Dr. Myles”
- ✅ Cache everything with Redis for speed and repeatability

---

## 📁 Project Structure Overview

The project is structured as follows:

```bash
inbound_ministry/
├── agents/
│   ├── api.py
│   ├── analytics.py
│   ├── escalation_detector.py
│   ├── faq_tool.py
│   ├── inbound_agent.py
│   ├── tone_polisher.py
│   └── utils.py
├── data/
│   ├── faqs.json
│   └── verses.json
├── main.py
├── requirements.txt
└── README.md
```

### `agents/` Directory

This directory contains all the Python scripts that make up the core functionality of the system.

- `api.py`: Defines the FastAPI endpoints for the system.
- `analytics.py`: Handles logging and analytics.
- `escalation_detector.py`: Detects sensitive topics that require human intervention.
- `faq_tool.py`: Handles FAQ retrieval using ChromaDB.
- `inbound_agent.py`: Orchestrates the entire message processing pipeline.
- `tone_polisher.py`: Polishes the tone of the responses.
- `utils.py`: Contains utility functions and setup.

### `data/` Directory

This directory contains the data used by the system.

- `faqs.json`: Contains the FAQs used for vector search.
- `verses.json`: Contains a list of verses for fallback scripture recommendations.

### `main.py`

This is the entry point for the application. It starts the FastAPI server.

### `requirements.txt`

This file contains the Python dependencies required to run the application.

### `README.md`

This file contains the project documentation you're reading now.

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Redis**: The system uses Redis for caching. You can download and install it from [redis.io](https://redis.io/download/).
3. **LM Studio**: The system uses LM Studio for local LLM inference. You can download it from [lmstudio.ai](https://lmstudio.ai/).
4. **OpenAI API Key**: You'll need an OpenAI API key for the escalation detection and scripture recommendation features.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   touch .env
   ```
   Add the following variables to the `.env` file:
   ```
   REDIS_HOST=localhost
   REDIS_PORT=6379
   LM_STUDIO_URL=http://localhost:1234/v1/chat/completions
   LM_MODEL_NAME=mythomax-13b
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the application:
   ```bash
   python main.py
   ```

The application should now be running at `http://localhost:8000`.

---

## 📝 API Endpoints
Swagger UI: http://localhost:8000/docs
OpenAPI JSON: http://localhost:8000/openapi.json

✅ Example: POST /tone-polish
Input:
json
Always show details


{
  "raw_response": "I don't know if God hears me anymore.",
  "context": "Person struggling with faith",
  "scripture": "Psalm 34:17"
}
Output:
json
Always show details


{
  "polished_response": "Beloved, even in your silence, the Lord hears your cry. As Psalm 34:17 assures us, 'The righteous cry out, and the Lord hears them.'"
}

---
## Dependencies
From requirements.txt
```bash
fastapi==0.116.0
uvicorn==0.35.0
openai==0.28.1
redis==6.2.0
python-dotenv==1.1.1

Optional enhancements:
chromadb==1.0.15
sentence-transformers==5.0.0
PyMuPDF==1.23.7
httpx==0.28.1
pandas==2.2.2

```

✅ Testing & QA Checklist

🧪 Environment & Setup
.env is configured

Redis is running locally

LM Studio is active with Mythomax model

requirements.txt is fully installed

⚙️ API Validation
 GET / health check passes

 POST /tone-polish returns styled response

 Response includes scripture integration

🧠 Redis Caching
 Repeat queries hit cache (check logs or timing)

 Redis keys like tone:<hash> or faq:<hash> are present

📚 FAQ Tool
 data/faqs.json is loaded

 Vector matching returns relevant answers for similar questions

🧹 Error Handling
 LM Studio down triggers fallback

 Redis unavailable logs warning

 Missing .env raises clear error

🚧 Known Notes
openai.api_base must be set to http://localhost:1234/v1

Works 100% offline using LM Studio + Redis

Escalation detection and analytics are modular

No authentication required for LM Studio setup

✅ Summary
✔️ Modular Agents
✔️ Redis Caching
✔️ Swagger Docs
✔️ Environment Driven
✔️ Vector Search + Tone Polishing






 *Everything's ready for local use or next-stage productionization.*

**— Sage**



