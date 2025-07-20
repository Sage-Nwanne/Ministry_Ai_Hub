# Ministry AI Hub - Professional Communication Platform

> **Enterprise-grade AI-driven ministry communication system** that provides intelligent, contextual responses to inbound messages while maintaining pastoral care standards and donor engagement excellence.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.0-green.svg)](https://fastapi.tiangolo.com)
[![Swarms](https://img.shields.io/badge/Swarms-5.0+-purple.svg)](https://github.com/kyegomez/swarms)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

The Ministry AI Hub is a comprehensive communication platform featuring two specialized AI agent systems:

### 🔵 **Inbound Communications System** - *Digital Minister of First Impressions*
- **Process inquiries** from website, email, and contact forms
- **Detect sensitive content** requiring human pastoral intervention
- **Provide FAQ responses** with enhanced, personalized answers
- **Multilingual support** for global ministry outreach (English, Spanish, French, Portuguese, German)
- **Prayer request routing** with deliverance session scheduling
- **Maintain Dr. Myles' authentic pastoral voice** in all communications

### 🟢 **Donation Engagement System** - *Digital Stewardship Companion*
- **Generate personalized thank-you messages** with scripture-based gratitude
- **Share compelling impact stories** highlighting ministry achievements
- **Promote biblical stewardship** and recurring giving opportunities
- **Answer donation questions** including tax deductibility and giving methods

---

## 🏗️ **System Architecture**

```
Ministry AI Hub/
├── ministry_hub_main.py           # Main FastAPI application
├── agents/                        # AI Agent Systems
│   ├── inbound/                   # Inbound Communications
│   │   ├── api.py                 # Inbound API routes
│   │   ├── inbound_agent.py       # Main message processor
│   │   └── swarm_agents.py        # Specialized AI agents
│   ├── donation/                  # Donation Engagement
│   │   ├── api.py                 # Donation API routes
│   │   └── donation_agents.py     # Donation AI agents
│   └── shared/                    # Shared Components
│       ├── analytics.py           # Interaction logging
│       ├── faq_tool.py           # FAQ system
│       └── utils.py              # Utility functions
├── data/                          # Data Files
│   ├── faq_data.json             # FAQ database
│   └── impact_stories.json       # Impact story templates
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
└── README.md                      # This file
```

---

## 🚀 **Quick Start Guide**

### **Prerequisites**
- **Python 3.8+** installed
- **Redis Server** for caching
- **OpenAI API Key** for AI functionality
- **Git** for repository management

### **Step 1: Repository Setup**

```bash
# Clone the repository
git clone https://github.com/Sage-Nwanne/inbound_ministry_clean.git
cd inbound_ministry_clean

# Verify Python version
python --version  # Should be 3.8+
```

### **Step 2: Environment Setup**

```bash
# Create virtual environment
python -m venv ministry_env

# Activate virtual environment
# Windows:
ministry_env\Scripts\activate
# macOS/Linux:
source ministry_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 3: Configuration**

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
nano .env  # or your preferred editor
```

**Required `.env` configuration:**
```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Redis Configuration (optional - defaults work locally)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Logging Configuration
LOG_LEVEL=INFO
```

### **Step 4: Redis Setup**

**Option A: Local Redis**
```bash
# Install Redis (varies by OS)
# Ubuntu/Debian:
sudo apt-get install redis-server

# macOS (Homebrew):
brew install redis

# Start Redis
redis-server
```

**Option B: Docker Redis**
```bash
# Run Redis in Docker
docker run -d -p 6379:6379 --name ministry-redis redis:alpine
```

**Verify Redis:**
```bash
redis-cli ping  # Should return: PONG
```

### **Step 5: Launch Ministry Hub**

```bash
# Start the Ministry AI Hub
python ministry_hub_main.py
```

**Expected output:**
```
🚀 Starting Ministry AI Hub...
✅ Environment validation passed
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### **Step 6: Verify Installation**

**Access points:**
- **Main Hub:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

---

## 🧪 **API Testing**

### **Inbound Communications Tests**

```bash
# Test message processing
curl -X POST http://localhost:8000/api/v1/inbound/process \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I need prayer for my family",
    "user_id": "test_user",
    "source": "website",
    "language": "en"
  }'

# Test multilingual translation
curl -X POST http://localhost:8000/api/v1/inbound/translate \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I need prayer for healing",
    "target_language": "es"
  }'

# Test prayer request routing
curl -X POST http://localhost:8000/api/v1/inbound/prayer \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Please pray for my healing",
    "user_id": "prayer_user",
    "urgency": "normal"
  }'

# Test FAQ lookup
curl -X POST http://localhost:8000/api/v1/inbound/faq \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are your service times?",
    "user_id": "faq_user",
    "language": "en"
  }'
```

### **Donation Engagement Tests**

```bash
# Test thank-you message generation
curl -X POST http://localhost:8000/api/v1/donation/thank-you \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "John Smith",
    "amount": "$100",
    "email": "john@example.com"
  }'

# Test impact story generation
curl -X POST http://localhost:8000/api/v1/donation/impact-story \
  -H "Content-Type: application/json" \
  -d '{
    "category": "youth",
    "donor_segment": "regular_donor"
  }'

# Test recurring giving promotion
curl -X POST http://localhost:8000/api/v1/donation/recurring \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Jane Doe",
    "current_amount": "$50",
    "suggested_frequency": "monthly"
  }'

# Test donation Q&A
curl -X POST http://localhost:8000/api/v1/donation/qa \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Is my donation tax deductible?",
    "donor_context": "first_time_donor"
  }'
```

---

## 📊 **Interactive API Documentation**

Access comprehensive API documentation:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Features:
- ✅ Interactive endpoint testing
- ✅ Request/response schemas
- ✅ Parameter documentation
- ✅ Code examples for integration

---

## 🌍 **Supported Languages**

| Language | Code | Status |
|----------|------|--------|
| English | `en` | ✅ Primary |
| Spanish | `es` | ✅ Supported |
| French | `fr` | ✅ Supported |
| Portuguese | `pt` | ✅ Supported |
| German | `de` | ✅ Supported |

---

## 🔧 **Troubleshooting**

### **Common Issues**

**"OpenAI API key not found"**
```bash
# Verify .env file
cat .env | grep OPENAI_API_KEY
# Ensure key is properly set without quotes
```

**"Redis connection failed"**
```bash
# Check Redis status
redis-cli ping
# If not running:
redis-server
```

**"Port 8000 already in use"**
```bash
# Use different port
python ministry_hub_main.py --port 8001
# Or kill existing process
lsof -ti:8000 | xargs kill -9
```

**"Module not found errors"**
```bash
# Ensure virtual environment is active
source ministry_env/bin/activate  # Linux/macOS
ministry_env\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**"FAQ data not found"**
```bash
# Ensure data directory exists
mkdir -p data
# Create basic FAQ file if missing
echo '{"faqs": []}' > data/faq_data.json
```

---

## 🎯 **Key Features**

### **Inbound Communications**
- ✅ **Escalation Detection** - Identifies sensitive topics requiring human intervention
- ✅ **Scripture Integration** - Provides relevant biblical guidance
- ✅ **Multilingual Support** - Processes messages in 5 languages
- ✅ **Prayer Routing** - Directs prayer requests to appropriate ministry teams
- ✅ **FAQ Enhancement** - Personalizes standard answers with pastoral tone
- ✅ **Dr. Myles Voice** - Maintains authentic pastoral communication style

### **Donation Engagement**
- ✅ **Personalized Thank-You** - Scripture-based gratitude messages
- ✅ **Impact Stories** - Compelling ministry achievement narratives
- ✅ **Stewardship Promotion** - Biblical giving encouragement
- ✅ **Donation Q&A** - Comprehensive giving information

### **System Features**
- ✅ **Real-time Processing** - Instant message handling
- ✅ **Analytics Logging** - Comprehensive interaction tracking
- ✅ **Modular Architecture** - Easy maintenance and expansion
- ✅ **API-First Design** - Simple integration with existing systems

---

## 📈 **Next Steps**

1. **📋 Explore API Documentation** - http://localhost:8000/docs
2. **🧪 Test All Endpoints** - Use the interactive interface
3. **⚙️ Configure Ministry Data** - Update `data/` directory files
4. **🔗 Integrate Systems** - Connect to your existing platforms
5. **📊 Monitor Analytics** - Review interaction logs
6. **🚀 Deploy to Production** - Follow deployment best practices

---

## 💡 **Support & Resources**

- **📖 Documentation:** Available in `/docs` directory
- **🐛 Issues:** [GitHub Issues](https://github.com/Sage-Nwanne/inbound_ministry_clean/issues)
- **💬 Discussions:** [GitHub Discussions](https://github.com/Sage-Nwanne/inbound_ministry_clean/discussions)
- **📧 Support:** Contact your system administrator

---

**Version:** 2.0.0 | **Framework:** Swarms AI + FastAPI | **Status:** Production Ready

*Empowering ministry through intelligent automation while preserving the human touch.*



