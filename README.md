# Ministry AI Hub - Professional Communication Platform

> **Enterprise-grade AI-driven ministry communication system** that provides intelligent, contextual responses to inbound messages while maintaining pastoral care standards and donor engagement excellence.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.0-green.svg)](https://fastapi.tiangolo.com)
[![Swarms](https://img.shields.io/badge/Swarms-5.0+-purple.svg)](https://github.com/kyegomez/swarms)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-1.74+-orange.svg)](https://github.com/BerriAI/litellm)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

The Ministry AI Hub is a comprehensive communication platform featuring two specialized AI agent systems powered by **LM Studio** and **Swarms AI Framework**:

### 🔵 **Inbound Communications System** - *Digital Minister of First Impressions*
- **Process inquiries** from website, email, and contact forms with intelligent routing
- **Detect sensitive content** requiring human pastoral intervention (safety-first approach)
- **Provide FAQ responses** with enhanced, personalized answers using Dr. Myles' voice
- **Multilingual support** for global ministry outreach (English, Spanish, French, Portuguese, German)
- **Prayer request routing** with deliverance session scheduling and ministry team coordination
- **Maintain Dr. Myles' authentic pastoral voice** in all communications

### 🟢 **Donation Engagement System** - *Digital Stewardship Companion*
- **Generate personalized thank-you messages** with scripture-based gratitude and donor recognition
- **Share compelling impact stories** highlighting ministry achievements and transformation
- **Promote biblical stewardship** and recurring giving opportunities with spiritual growth focus
- **Answer donation questions** including tax deductibility, giving methods, and planned giving

---

## 🏗️ **System Architecture**

```
Ministry AI Hub/
├── ministry_hub_main.py           # Main FastAPI application & server
├── agents/                        # AI Agent Systems
│   ├── inbound/                   # Inbound Communications
│   │   ├── api.py                 # Inbound API routes & endpoints
│   │   ├── inbound_agent.py       # Main message processor with smart routing
│   │   └── swarm_agents.py        # Specialized AI agents (escalation, scripture, etc.)
│   ├── donation/                  # Donation Engagement
│   │   ├── api.py                 # Donation API routes & endpoints
│   │   └── donation_agents.py     # Donation AI agents (thank-you, impact, etc.)
│   └── shared/                    # Shared Components
│       ├── analytics.py           # Interaction logging & metrics
│       ├── faq_tool.py           # FAQ system with ChromaDB
│       └── utils.py              # Utility functions & helpers
├── data/                          # Data Files
│   ├── faq_data.json             # FAQ database with ministry information
│   └── impact_stories.json       # Impact story templates by category
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template with all variables
├── test_donation_endpoints.sh     # Automated testing script
└── README.md                      # This comprehensive guide
```

---

## 🚀 **Quick Start Guide**

### **Prerequisites**
- **Python 3.8+** installed and accessible
- **LM Studio** running locally with Qwen model
- **Redis Server** for caching and session management
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

### **Step 3: LM Studio Configuration**

**Install and Setup LM Studio:**
1. Download [LM Studio](https://lmstudio.ai/) for your platform
2. Install and launch LM Studio
3. Download the **Qwen 3 4B** model (recommended for ministry use)
4. Start the local server on port `1234` (default)
5. Verify server is running at `http://localhost:1234`

**Test LM Studio Connection:**
```bash
# Test if LM Studio is responding
curl http://localhost:1234/v1/models
```

### **Step 4: Environment Configuration**

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
nano .env  # or your preferred editor
```

**Complete `.env` configuration:**
```env
# LM Studio Configuration (Primary AI Provider)
LM_STUDIO_API_BASE=http://192.168.1.88:1234/v1  # Update with your LM Studio IP
LM_STUDIO_API_KEY=lm-studio                      # Default LM Studio key
LM_STUDIO_MODEL=openai/qwen3-4b:2               # Model name in LM Studio

# OpenAI Configuration (Fallback - Optional)
OPENAI_API_KEY=your_openai_api_key_here         # Optional fallback

# Redis Configuration
REDIS_HOST=localhost                             # Redis server host
REDIS_PORT=6379                                 # Redis server port
REDIS_DB=0                                      # Redis database number
REDIS_PASSWORD=                                 # Redis password (if required)

# Application Configuration
LOG_LEVEL=INFO                                  # Logging level (DEBUG, INFO, WARNING, ERROR)
ENVIRONMENT=development                         # Environment (development, staging, production)
API_VERSION=v1                                  # API version prefix

# Security Configuration
SECRET_KEY=your-secret-key-here                 # For session management
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000  # CORS origins

# Ministry Configuration
MINISTRY_NAME=Dr. Myles Ministry                # Your ministry name
PASTOR_NAME=Dr. Myles                          # Pastor's name for personalization
MINISTRY_EMAIL=contact@ministry.org            # Ministry contact email
MINISTRY_PHONE=+1-555-123-4567                # Ministry phone number

# Analytics & Monitoring
ENABLE_ANALYTICS=true                          # Enable interaction logging
ANALYTICS_RETENTION_DAYS=90                    # How long to keep analytics data

# Feature Flags
ENABLE_MULTILINGUAL=true                       # Enable translation features
ENABLE_PRAYER_ROUTING=true                     # Enable prayer request routing
ENABLE_ESCALATION_DETECTION=true               # Enable sensitive content detection
ENABLE_DONATION_TRACKING=true                  # Enable donation engagement features
```

### **Step 5: Redis Setup**

**Option A: Local Redis Installation**
```bash
# Install Redis (varies by OS)
# Ubuntu/Debian:
sudo apt-get update && sudo apt-get install redis-server

# macOS (Homebrew):
brew install redis

# Windows: Download from https://redis.io/download

# Start Redis service
# Linux/macOS:
redis-server
# Windows: Run redis-server.exe
```

**Option B: Docker Redis (Recommended)**
```bash
# Run Redis in Docker container
docker run -d \
  --name ministry-redis \
  -p 6379:6379 \
  --restart unless-stopped \
  redis:alpine

# Verify Redis is running
docker ps | grep ministry-redis
```

**Verify Redis Connection:**
```bash
redis-cli ping  # Should return: PONG
```

### **Step 6: Data Files Setup**

**Create FAQ Data File:**
```bash
# Ensure data directory exists
mkdir -p data

# Create basic FAQ file
cat > data/faq_data.json << 'EOF'
{
  "faqs": [
    {
      "question": "What are your service times?",
      "answer": "We have services on Sunday at 9:00 AM and 11:00 AM, and Wednesday evening at 7:00 PM.",
      "category": "services",
      "keywords": ["service", "times", "schedule", "sunday", "wednesday"]
    },
    {
      "question": "How can I get baptized?",
      "answer": "Baptism is a beautiful step of faith! Please speak with Pastor or attend our baptism class held monthly.",
      "category": "baptism",
      "keywords": ["baptism", "baptized", "water", "faith"]
    },
    {
      "question": "Do you have children's ministry?",
      "answer": "Yes! We have vibrant children's programs for ages 0-12 during all services, plus special events throughout the year.",
      "category": "children",
      "keywords": ["children", "kids", "youth", "nursery"]
    }
  ]
}
EOF
```

**Create Impact Stories File:**
```bash
cat > data/impact_stories.json << 'EOF'
{
  "youth": [
    {
      "title": "Youth Ministry Transformation",
      "description": "Our youth program has grown by 40% this year, reaching 150 young people weekly with mentorship, biblical teaching, and life skills training.",
      "impact": "40% growth, 150 youth reached weekly",
      "metrics": {
        "participants": 150,
        "growth_rate": "40%",
        "weekly_attendance": 120
      }
    }
  ],
  "seniors": [
    {
      "title": "Senior Care Ministry",
      "description": "Monthly visits to 80 seniors in our community, providing companionship, prayer, practical support, and grocery assistance.",
      "impact": "80 seniors served monthly",
      "metrics": {
        "seniors_served": 80,
        "monthly_visits": 320,
        "volunteer_hours": 240
      }
    }
  ],
  "missions": [
    {
      "title": "Global Missions Impact",
      "description": "Supporting 12 missionary families across 8 countries, providing clean water to 500 families, and building 3 schools this year.",
      "impact": "12 missionaries, 8 countries, 500 families served",
      "metrics": {
        "missionaries": 12,
        "countries": 8,
        "families_served": 500,
        "schools_built": 3
      }
    }
  ],
  "general": [
    {
      "title": "Community Outreach",
      "description": "Food pantry serving 200 families monthly, job training programs, and community events bringing hope to our neighborhood.",
      "impact": "200 families fed monthly",
      "metrics": {
        "families_fed": 200,
        "food_boxes": 800,
        "job_placements": 25
      }
    }
  ]
}
EOF
```

### **Step 7: Launch Ministry Hub**

```bash
# Start the Ministry AI Hub
python ministry_hub_main.py

# Alternative: Run with custom port
python ministry_hub_main.py --port 8001

# Alternative: Run with uvicorn directly
uvicorn ministry_hub_main:app --host 0.0.0.0 --port 8000 --reload
```

**Expected startup output:**
```
🚀 Starting Ministry AI Hub...
✅ Environment validation passed
✅ LM Studio connection verified
✅ Redis connection established
✅ Data files loaded successfully
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### **Step 8: Verify Installation**

**Access points:**
- **Main Hub:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health
- **System Status:** http://localhost:8000/status

---

## 🧪 **Comprehensive API Testing**

### **Inbound Communications Tests**

**1. Basic Message Processing:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/process \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I need prayer for my family",
    "user_id": "test_user_001",
    "source": "website",
    "language": "en"
  }'
```

**2. Escalation Detection Test:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/process \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I am feeling very depressed and having dark thoughts",
    "user_id": "test_user_002",
    "source": "email",
    "language": "en"
  }'
```

**3. Multilingual Translation Test:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/translate \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I need prayer for healing",
    "target_language": "es"
  }'
```

**4. Prayer Request Routing:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/prayer \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Please pray for my healing from cancer",
    "user_id": "prayer_user_001",
    "urgency": "high",
    "contact_info": "john@example.com"
  }'
```

**5. FAQ Lookup Test:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/faq \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are your service times?",
    "user_id": "faq_user_001",
    "language": "en"
  }'
```

### **Donation Engagement Tests**

**1. Thank-You Message Generation:**
```bash
# First-time donor
curl -X POST http://localhost:8000/api/v1/donation/thank-you \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Sarah Johnson",
    "amount": "$50",
    "email": "sarah.johnson@email.com",
    "donation_type": "first_time"
  }'

# Major gift donor
curl -X POST http://localhost:8000/api/v1/donation/thank-you \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Robert and Mary Williams",
    "amount": "$2,500",
    "email": "rwilliams@email.com",
    "donation_type": "major_gift"
  }'
```

**2. Impact Story Generation:**
```bash
# Youth ministry impact
curl -X POST http://localhost:8000/api/v1/donation/impact-story \
  -H "Content-Type: application/json" \
  -d '{
    "category": "youth",
    "donor_segment": "regular_donor"
  }'

# Missions impact
curl -X POST http://localhost:8000/api/v1/donation/impact-story \
  -H "Content-Type: application/json" \
  -d '{
    "category": "missions",
    "donor_segment": "major_donor"
  }'
```

**3. Recurring Giving Promotion:**
```bash
curl -X POST http://localhost:8000/api/v1/donation/recurring \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Michael Thompson",
    "current_amount": "$75",
    "suggested_frequency": "monthly",
    "donor_history": "6_months"
  }'
```

**4. Donation Q&A:**
```bash
# Tax deductibility
curl -X POST http://localhost:8000/api/v1/donation/qa \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Is my donation tax deductible?",
    "donor_context": "first_time_donor"
  }'

# Giving methods
curl -X POST http://localhost:8000/api/v1/donation/qa \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the different ways I can give?",
    "donor_context": "regular_donor"
  }'

# Planned giving
curl -X POST http://localhost:8000/api/v1/donation/qa \
  -H "Content-Type: application/json" \
  -d '{
    "question": "How can I include the ministry in my will?",
    "donor_context": "major_donor"
  }'
```

### **Automated Testing Script**

Create comprehensive test script:

```bash
# Make test script executable
chmod +x test_all_endpoints.sh

# Run all tests
./test_all_endpoints.sh
```

---

## 📊 **Interactive API Documentation**

Access comprehensive API documentation with live testing:

- **Swagger UI:** http://localhost:8000/docs
  - ✅ Interactive endpoint testing
  - ✅ Request/response schemas
  - ✅ Parameter documentation
  - ✅ Authentication testing

- **ReDoc:** http://localhost:8000/redoc
  - ✅ Clean, readable documentation
  - ✅ Code examples
  - ✅ Schema exploration

**Key API Features:**
- **Authentication:** Bearer token support
- **Rate Limiting:** Built-in request throttling
- **Error Handling:** Comprehensive error responses
- **Validation:** Automatic request validation
- **Logging:** Full request/response logging

---

## 🌍 **Multilingual Support**

| Language | Code | Status | Test Command |
|----------|------|--------|--------------|
| English | `en` | ✅ Primary | `"language": "en"` |
| Spanish | `es` | ✅ Supported | `"language": "es"` |
| French | `fr` | ✅ Supported | `"language": "fr"` |
| Portuguese | `pt` | ✅ Supported | `"language": "pt"` |
| German | `de` | ✅ Supported | `"language": "de"` |

**Translation Test:**
```bash
curl -X POST http://localhost:8000/api/v1/inbound/translate \
  -H "Content-Type: application/json" \
  -d '{
    "message": "God bless you and your family",
    "target_language": "es"
  }'
```

---

## 🔧 **Troubleshooting Guide**

### **Common Issues & Solutions**

**1. "LM Studio connection failed"**
```bash
# Check LM Studio status
curl http://localhost:1234/v1/models

# Verify LM Studio is running
ps aux | grep lmstudio  # Linux/macOS
tasklist | findstr lmstudio  # Windows

# Update IP address in .env if needed
LM_STUDIO_API_BASE=http://YOUR_IP:1234/v1
```

**2. "Redis connection failed"**
```bash
# Check Redis status
redis-cli ping

# Start Redis if not running
redis-server  # Local installation
docker start ministry-redis  # Docker installation

# Check Redis logs
redis-cli monitor
```

**3. "Port 8000 already in use"**
```bash
# Find process using port 8000
lsof -ti:8000  # Linux/macOS
netstat -ano | findstr :8000  # Windows

# Kill existing process
kill -9 $(lsof -ti:8000)  # Linux/macOS

# Use different port
python ministry_hub_main.py --port 8001
```

**4. "Module not found errors"**
```bash
# Ensure virtual environment is active
source ministry_env/bin/activate  # Linux/macOS
ministry_env\Scripts\activate     # Windows

# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Check Python path
python -c "import sys; print(sys.path)"
```

**5. "FAQ/Impact data not found"**
```bash
# Ensure data directory exists
mkdir -p data

# Recreate data files (see Step 6 above)
# Or check file permissions
ls -la data/
chmod 644 data/*.json
```

**6. "AI Agent timeout errors"**
```bash
# Check LM Studio model is loaded
curl http://localhost:1234/v1/models

# Verify model name in .env matches LM Studio
LM_STUDIO_MODEL=openai/qwen3-4b:2

# Increase timeout in agent configuration
# Edit agents/*/agents.py files
```

### **Performance Optimization**

**1. Reduce Response Times:**
- Use smaller AI models for faster responses
- Enable Redis caching for FAQ responses
- Implement response caching for common queries

**2. Scale for Production:**
- Use multiple LM Studio instances
- Implement load balancing
- Add database for persistent storage

**3. Monitor System Health:**
```bash
# Check system resources
htop  # Linux/macOS
taskmgr  # Windows

# Monitor API performance
curl http://localhost:8000/health
curl http://localhost:8000/metrics  # If enabled
```

---

## 🎯 **Key Features & Capabilities**

### **Inbound Communications**
- ✅ **Smart Agent Routing** - Messages routed to appropriate agents for efficiency
- ✅ **Escalation Detection** - AI identifies sensitive topics requiring human intervention
- ✅ **Scripture Integration** - Contextual biblical guidance with every response
- ✅ **Multilingual Support** - Processes and responds in 5 languages
- ✅ **Prayer Routing** - Intelligent prayer request categorization and routing
- ✅ **FAQ Enhancement** - Personalizes standard answers with pastoral tone
- ✅ **Dr. Myles Voice** - Maintains authentic pastoral communication style
- ✅ **Safety First** - Comprehensive content filtering and escalation protocols

### **Donation Engagement**
- ✅ **Personalized Thank-You** - Scripture-based gratitude with donor recognition
- ✅ **Impact Stories** - Compelling ministry achievement narratives by category
- ✅ **Stewardship Promotion** - Biblical giving encouragement and education
- ✅ **Donation Q&A** - Comprehensive giving information and tax guidance
- ✅ **Recurring Giving** - Intelligent promotion of sustainable giving patterns
- ✅ **Donor Segmentation** - Tailored messaging based on giving history

### **System Features**
- ✅ **Real-time Processing** - Sub-10 second response times with smart routing
- ✅ **Analytics Logging** - Comprehensive interaction tracking and metrics
- ✅ **Modular Architecture** - Easy maintenance, testing, and feature expansion
- ✅ **API-First Design** - RESTful APIs for seamless integration
- ✅ **Production Ready** - Error handling, logging, monitoring, and scaling support
- ✅ **Security Focused** - Input validation, rate limiting, and secure configurations

---

## 🚀 **Production Deployment**

### **Environment Setup**
```bash
# Production environment variables
ENVIRONMENT=production
LOG_LEVEL=WARNING
ENABLE_ANALYTICS=true
REDIS_PASSWORD=your-secure-redis-password
SECRET_KEY=your-production-secret-key
```

### **Docker Deployment**
```dockerfile
# Dockerfile example
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "ministry_hub_main.py"]
```

### **Monitoring & Logging**
- **Health Checks:** `/health`, `/status` endpoints
- **Metrics:** Request counts, response times, error rates
- **Logging:** Structured JSON logs with correlation IDs
- **Alerts:** Integration with monitoring systems

---

## 📈 **Next Steps & Roadmap**

### **Immediate Actions**
1. **📋 Explore API Documentation** - http://localhost:8000/docs
2. **🧪 Test All Endpoints** - Run comprehensive test suite
3. **⚙️ Configure Ministry Data** - Customize FAQ and impact stories
4. **🔗 Integrate Systems** - Connect to existing ministry platforms
5. **📊 Monitor Analytics** - Review interaction logs and metrics

### **Future Enhancements**
- **📱 Mobile App Integration** - React Native/Flutter support
- **🎤 Voice Integration** - Speech-to-text and text-to-speech
- **📧 Email Integration** - Direct email processing and responses
- **📅 Calendar Integration** - Appointment scheduling for pastoral care
- **💾 Database Integration** - PostgreSQL/MongoDB for data persistence
- **🔐 Advanced Security** - OAuth2, JWT tokens, role-based access

---

## 💡 **Support & Resources**

### **Documentation & Help**
- **📖 API Documentation:** http://localhost:8000/docs
- **🔧 Configuration Guide:** See environment variables section above
- **🧪 Testing Guide:** See API testing section above
- **🐛 Issue Reporting:** [GitHub Issues](https://github.com/Sage-Nwanne/inbound_ministry_clean/issues)
- **💬 Community:** [GitHub Discussions](https://github.com/Sage-Nwanne/inbound_ministry_clean/discussions)

### **Technical Support**
- **📧 Email Support:** Contact your system administrator
- **📱 Emergency Contact:** For production issues
- **🎓 Training:** Available for ministry staff
- **🔄 Updates:** Regular feature updates and security patches

### **Contributing**
- **🤝 Contributions Welcome:** Fork, improve, submit PR
- **📝 Documentation:** Help improve this README
- **🧪 Testing:** Add test cases and scenarios
- **🐛 Bug Reports:** Detailed issue reports appreciated

---

**Version:** 2.1.0 | **Framework:** Swarms AI + FastAPI + LiteLLM | **Status:** Production Ready

*Empowering ministry through intelligent automation while preserving the human touch of pastoral care.*

---

## 📋 **Quick Reference**

### **Essential Commands**
```bash
# Start system
python ministry_hub_main.py

# Test health
curl http://localhost:8000/health

# View logs
tail -f ministry_hub.log

# Test prayer request
curl -X POST http://localhost:8000/api/v1/inbound/process \
  -H "Content-Type: application/json" \
  -d '{"message": "Please pray for me", "user_id": "test"}'
```

### **Key URLs**
- **Main API:** http://localhost:8000
- **Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health
- **LM Studio:** http://localhost:1234
- **Redis:** localhost:6379

### **Important Files**
- **Configuration:** `.env`
- **FAQ Data:** `data/faq_data.json`
- **Impact Stories:** `data/impact_stories.json`
- **Main App:** `ministry_hub_main.py`
- **Requirements:** `requirements.txt`



