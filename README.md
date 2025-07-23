# Ministry AI Hub - Professional Communication Platform

> **Enterprise-grade AI-driven ministry communication system** that provides intelligent, contextual responses to inbound messages while maintaining pastoral care standards and donor engagement excellence.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.0-green.svg)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-15.4.3-black.svg)](https://nextjs.org)
[![React](https://img.shields.io/badge/React-19.1.0-blue.svg)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://typescriptlang.org)
[![Swarms](https://img.shields.io/badge/Swarms-5.0+-purple.svg)](https://github.com/kyegomez/swarms)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-1.74+-orange.svg)](https://github.com/BerriAI/litellm)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

The Ministry AI Hub is a comprehensive communication platform featuring two specialized AI agent systems powered by **LM Studio** and **Swarms AI Framework**, with a modern **Next.js frontend** for seamless user interaction:

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

### 🎨 **Modern Frontend Interface** - *Professional Ministry Dashboard*
- **Responsive web application** built with Next.js 15 and React 19
- **Real-time chat interface** for AI-powered ministry conversations
- **Sermon insights dashboard** with transcript management and key takeaways
- **Donation flow management** with stewardship companion features
- **Analytics dashboard** for ministry effectiveness tracking
- **Mobile-optimized design** with ministry branding and accessibility

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
├── ministry-ai-hub-frontend/      # Next.js Frontend Application
│   ├── src/
│   │   ├── app/                   # Next.js App Router pages
│   │   │   ├── page.tsx           # Dashboard homepage
│   │   │   ├── chat/              # Chat interface pages
│   │   │   ├── summaries/         # Sermon insights pages
│   │   │   ├── donations/         # Donation flow pages
│   │   │   └── analytics/         # Analytics dashboard pages
│   │   ├── components/            # React components
│   │   │   ├── layout/            # Header, Sidebar, Navigation
│   │   │   ├── chat/              # Chat interface components
│   │   │   ├── summaries/         # Sermon management components
│   │   │   └── donations/         # Donation flow components
│   │   └── data/                  # Mock data and TypeScript interfaces
│   ├── package.json               # Frontend dependencies
│   ├── tailwind.config.ts         # Tailwind CSS configuration
│   └── next.config.ts             # Next.js configuration
├── data/                          # Backend Data Files
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
- **Node.js 18.17+** for the frontend application
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

# Verify Node.js version
node --version     # Should be 18.17+
```

### **Step 2: Backend Environment Setup**

```bash
# Create virtual environment
python -m venv ministry_env

# Activate virtual environment
# Windows:
ministry_env\Scripts\activate
# macOS/Linux:
source ministry_env/bin/activate

# Install backend dependencies
pip install -r requirements.txt
```

### **Step 3: Frontend Environment Setup**

```bash
# Navigate to frontend directory
cd ministry-ai-hub-frontend

# Install frontend dependencies
npm install
# or
yarn install
# or
pnpm install

# Return to root directory
cd ..
```

### **Step 4: LM Studio Configuration**

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

### **Step 5: Environment Configuration**

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

### **Step 6: Redis Setup**

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

### **Step 7: Launch Ministry Hub Backend**

```bash
# Ensure virtual environment is activated
source ministry_env/bin/activate  # Linux/macOS
ministry_env\Scripts\activate     # Windows

# Start the Ministry AI Hub backend
python ministry_hub_main.py

# Alternative: Run with custom port
python ministry_hub_main.py --port 8001

# Alternative: Run with uvicorn directly
uvicorn ministry_hub_main:app --host 0.0.0.0 --port 8000 --reload
```

**Expected backend startup output:**
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

### **Step 8: Launch Ministry Hub Frontend**

**Open a new terminal window/tab:**

```bash
# Navigate to frontend directory
cd ministry-ai-hub-frontend

# Start the Next.js development server
npm run dev
# or
yarn dev
# or
pnpm dev

# Alternative: Start with Turbopack (faster)
npm run dev --turbopack
```

**Expected frontend startup output:**
```
▲ Next.js 15.4.3
- Local:        http://localhost:3000
- Environments: .env.local

✓ Starting...
✓ Ready in 2.1s
```

### **Step 9: Verify Complete Installation**

**Backend Access Points:**
- **Main API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health
- **System Status:** http://localhost:8000/status

**Frontend Access Points:**
- **Main Dashboard:** http://localhost:3000
- **Digital Minister Chat:** http://localhost:3000/chat
- **Sermon Insights:** http://localhost:3000/summaries
- **Stewardship Companion:** http://localhost:3000/donations
- **Impact Dashboard:** http://localhost:3000/analytics

---

## 🎨 **Frontend Navigation Guide**

### **Main Dashboard** (`/`)
- **Overview Cards:** Quick stats and system status
- **Module Navigation:** Access all four main features
- **Recent Activity:** Latest interactions and updates
- **Quick Actions:** Common tasks and shortcuts

### **Digital Minister Chat** (`/chat`)
- **Conversation List:** Manage multiple chat sessions
- **AI Chat Interface:** Real-time messaging with ministry AI
- **Scripture Integration:** Contextual biblical guidance
- **Escalation Detection:** Automatic routing for sensitive topics
- **Quick Replies:** Pre-configured response options
- **Language Support:** Multilingual conversation capabilities

### **Sermon Insights** (`/summaries`)
- **Sermon Grid:** Browse all sermon summaries
- **Detailed View:** Expandable cards with full transcripts
- **Key Takeaways:** Highlighted main points and lessons
- **Download Options:** PDF export and sharing capabilities
- **Search & Filter:** Find sermons by topic, speaker, or date
- **Tags System:** Categorized content for easy navigation

### **Stewardship Companion** (`/donations`)
- **4-Step Flow:** Guided donation engagement process
  1. **Donor Information:** Capture donor details and preferences
  2. **Thank You Generation:** AI-powered personalized gratitude messages
  3. **Impact Stories:** Share ministry achievements and transformations
  4. **Follow-up Planning:** Schedule recurring giving and stewardship
- **Message Preview:** Real-time preview of generated content
- **Scripture Integration:** Biblical stewardship principles
- **Donor Segmentation:** Tailored messaging by donor type

### **Impact Dashboard** (`/analytics`)
- **Ministry Metrics:** Comprehensive analytics and insights
- **Interaction Tracking:** Monitor AI system performance
- **Engagement Analytics:** Donor and member engagement patterns
- **Growth Indicators:** Ministry effectiveness measurements
- **Custom Reports:** Exportable data and visualizations

---

## 🎨 **Frontend Features & Design**

### **Design System**
- **Ministry Branding:** Navy (#0A1F44) and Gold (#D4AF37) color palette
- **Typography:** Playfair Display for headings, Inter for body text
- **Responsive Design:** Mobile-first approach with breakpoint optimization
- **Accessibility:** WCAG 2.1 compliant with proper ARIA labels
- **Dark Mode Ready:** Prepared for future dark theme implementation

### **Interactive Elements**
- **Framer Motion Animations:** Smooth page transitions and micro-interactions
- **Loading States:** Skeleton screens and progress indicators
- **Real-time Updates:** Live chat and notification systems
- **Touch Optimization:** Mobile-friendly gestures and interactions
- **Keyboard Navigation:** Full keyboard accessibility support

### **Component Architecture**
- **Modular Design:** Reusable components with TypeScript interfaces
- **State Management:** SWR for data fetching and caching
- **Error Boundaries:** Graceful error handling and recovery
- **Performance Optimization:** Code splitting and lazy loading
- **SEO Optimization:** Meta tags and structured data

---

## 🔧 **Development Workflow**

### **Frontend Development Commands**

```bash
# Navigate to frontend directory
cd ministry-ai-hub-frontend

# Development server (with hot reload)
npm run dev

# Production build
npm run build

# Start production server
npm run start

# Lint code
npm run lint

# Type checking
npx tsc --noEmit
```

### **Backend Development Commands**

```bash
# Activate virtual environment
source ministry_env/bin/activate

# Start development server
python ministry_hub_main.py

# Run tests
python -m pytest

# Check code formatting
black . --check

# Install new dependencies
pip install package_name
pip freeze > requirements.txt
```

### **Full Stack Development**

**Terminal 1 - Backend:**
```bash
source ministry_env/bin/activate
python ministry_hub_main.py
```

**Terminal 2 - Frontend:**
```bash
cd ministry-ai-hub-frontend
npm run dev
```

**Terminal 3 - Redis (if local):**
```bash
redis-server
```

---

## 🧪 **Testing the Complete System**

### **Frontend Testing**

**1. Dashboard Navigation:**
- Visit http://localhost:3000
- Verify all module cards are clickable
- Check responsive design on different screen sizes

**2. Chat Interface:**
- Navigate to `/chat`
- Test message sending and receiving
- Verify conversation list functionality
- Check mobile sidebar behavior

**3. Sermon Management:**
- Go to `/summaries`
- Test card expansion and transcript viewing
- Verify download and share buttons
- Check search and filtering

**4. Donation Flow:**
- Access `/donations`
- Complete the 4-step donation process
- Verify message generation and preview
- Test form validation and navigation

### **Backend API Testing**

**1. Health Check:**
```bash
curl http://localhost:8000/health
```

**2. Chat Processing:**
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

**3. Donation Thank You:**
```bash
curl -X POST http://localhost:8000/api/v1/donation/thank-you \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Sarah Johnson",
    "amount": "$50",
    "email": "sarah.johnson@email.com",
    "donation_type": "first_time"
  }'
```

### **Integration Testing**

**1. Frontend-Backend Communication:**
- Ensure frontend can reach backend APIs
- Verify CORS configuration allows requests
- Test error handling for failed API calls

**2. Real-time Features:**
- Test chat message flow from frontend to backend
- Verify AI responses appear in frontend chat
- Check loading states and error messages

---

## 🔧 **Troubleshooting Guide**

### **Frontend Issues**

**1. "npm install fails"**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Try different package manager
yarn install
# or
pnpm install
```

**2. "Port 3000 already in use"**
```bash
# Find process using port 3000
lsof -ti:3000  # Linux/macOS
netstat -ano | findstr :3000  # Windows

# Kill existing process
kill -9 $(lsof -ti:3000)  # Linux/macOS

# Use different port
npm run dev -- --port 3001
```

**3. "TypeScript errors"**
```bash
# Check TypeScript configuration
npx tsc --noEmit

# Update TypeScript and types
npm update typescript @types/react @types/node

# Clear Next.js cache
rm -rf .next
npm run dev
```

### **Backend Issues**

**4. "LM Studio connection failed"**
```bash
# Check LM Studio status
curl http://localhost:1234/v1/models

# Update CORS origins in .env
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# Restart backend server
python ministry_hub_main.py
```

**5. "Frontend can't reach backend"**
```bash
# Verify backend is running
curl http://localhost:8000/health

# Check CORS configuration in ministry_hub_main.py
# Ensure allow_origins includes frontend URL

# Test direct API call
curl -X GET http://localhost:8000/api/v1/inbound/health
```

### **Integration Issues**

**6. "API calls failing from frontend"**
- Check browser console for CORS errors
- Verify API endpoints match between frontend and backend
- Ensure both servers are running on correct ports
- Test API endpoints directly with curl first

**7. "Styling issues"**
```bash
# Rebuild Tailwind CSS
cd ministry-ai-hub-frontend
npm run build

# Clear browser cache
# Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

# Check Tailwind configuration
npx tailwindcss --help
```

---

## 📈 **Next Steps & Roadmap**

### **Immediate Actions**
1. **🎨 Explore Frontend Interface** - http://localhost:3000
2. **📋 Test API Integration** - Verify frontend-backend communication
3. **🧪 Complete User Flows** - Test all four main modules end-to-end
4. **⚙️ Customize Ministry Data** - Update branding, content, and configurations
5. **🔗 Connect Real Data** - Replace mock data with live API connections
6. **📊 Monitor Performance** - Check both frontend and backend metrics

### **Frontend Enhancements**
- **🔐 Authentication System** - User login and role-based access
- **🌙 Dark Mode** - Complete dark theme implementation
- **📱 PWA Features** - Offline support and mobile app capabilities
- **🔔 Real-time Notifications** - WebSocket integration for live updates
- **📊 Advanced Analytics** - Interactive charts and data visualizations
- **🎤 Voice Integration** - Speech-to-text for chat interface

### **Backend Integrations**
- **💾 Database Integration** - PostgreSQL/MongoDB for data persistence
- **📧 Email Integration** - Direct email processing and responses
- **📅 Calendar Integration** - Appointment scheduling for pastoral care
- **🔐 Advanced Security** - OAuth2, JWT tokens, role-based access
- **📱 Mobile API** - Optimized endpoints for mobile applications

---

## 💡 **Support & Resources**

### **Documentation & Help**
- **🎨 Frontend Interface:** http://localhost:3000
- **📖 Backend API Documentation:** http://localhost:8000/docs
- **🔧 Configuration Guide:** See environment variables section above
- **🧪 Testing Guide:** See testing sections above
- **🐛 Issue Reporting:** [GitHub Issues](https://github.com/Sage-Nwanne/inbound_ministry_clean/issues)
- **💬 Community:** [GitHub Discussions](https://github.com/Sage-Nwanne/inbound_ministry_clean/discussions)

### **Development Resources**
- **Next.js Documentation:** https://nextjs.org/docs
- **React Documentation:** https://react.dev
- **TypeScript Handbook:** https://typescriptlang.org/docs
- **Tailwind CSS:** https://tailwindcss.com/docs
- **Framer Motion:** https://framer.com/motion
- **FastAPI Documentation:** https://fastapi.tiangolo.com

---

## 📋 **Quick Reference**

### **Essential Commands**
```bash
# Start backend
source ministry_env/bin/activate
python ministry_hub_main.py

# Start frontend (new terminal)
cd ministry-ai-hub-frontend
npm run dev

# Test health
curl http://localhost:8000/health

# Access frontend
open http://localhost:3000
```

### **Key URLs**
- **Frontend Dashboard:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health
- **LM Studio:** http://localhost:1234
- **Redis:** localhost:6379

### **Important Files**
- **Backend Configuration:** `.env`
- **Frontend Package:** `ministry-ai-hub-frontend/package.json`
- **Main Backend App:** `ministry_hub_main.py`
- **Main Frontend Page:** `ministry-ai-hub-frontend/src/app/page.tsx`
- **Tailwind Config:** `ministry-ai-hub-frontend/tailwind.config.ts`

---

**Version:** 3.0.0 | **Stack:** Next.js + React + FastAPI + Swarms AI | **Status:** Full Stack Ready

*Empowering ministry through intelligent automation with a modern, accessible interface while preserving the human touch of pastoral care.*

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



