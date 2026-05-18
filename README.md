🤖 Professional AI Interview Architect (Multi-Provider)
![alt text](https://img.shields.io/badge/Deployment-Render-brightgreen.svg)

![alt text](https://img.shields.io/badge/Docker-Ready-blue.svg)

![alt text](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)
An advanced, scalable AI-driven interview question generator. This system features a robust AI Router that intelligently manages requests across Google Gemini, Groq, and OpenRouter, ensuring high availability and cost-optimization.
🔗 Live Demo on Render
🌟 Key Features
Multi-LLM Routing: Intelligent failover and selection between Groq (LPU speed), Gemini (Contextual depth), and OpenRouter.
Topic Narrowing Engine: Custom prompt engineering to strictly enforce professional job-title validation.
Performance Caching: Integrated Redis layer to cache frequent job-role requests and reduce API latency.
Persistent Storage: PostgreSQL backend for storing generated question sets, role histories, and user sessions.
Full Containerization: Ready for production deployment via Docker and Docker Compose.
Automated Testing: Comprehensive test suite for ensuring AI response integrity and API stability.
🛠️ Advanced Tech Stack
Backend: Flask (Python), Flask-SQLAlchemy, Flask-Migrate
AI Integration: Google Gemini SDK, Groq SDK, OpenRouter API
Validation: Marshmallow (Schema) / Pydantic
Database & Cache: PostgreSQL, Redis
DevOps: Docker, Docker Compose, Gunicorn
Security: Python-Dotenv, Environment Variable Guarding
📂 System Architecture & Folder Structure
code
Text
ai-interview-question-generator/
├── app.py                # Application Entry Point
├── config.py             # Global Configurations (Dev/Prod/Test)
├── extensions.py         # Initialization of DB, Redis, and Plugins
├── models/               # SQLAlchemy Database Models
├── schema/               # Data Validation & Serialization (Marshmallow)
├── services/             # Core Logic (AI Router, Prompt Builder)
├── utils/                # Helper Functions (Regex, Logging)
├── tests/                # Unit & Integration Testing
├── static/ & templates/  # Vanilla JS Frontend & Jinja2 Templates
├── Dockerfile            # Container definition
├── docker-compose.yml    # Orchestration for Flask, Redis, & Postgres
└── requirements.txt      # Project Dependencies
🚀 Installation & Local Development
Using Docker (Recommended)
code
Bash
docker-compose up --build
Manual Setup
Clone & Virtual Env:
code
Bash
git clone https://github.com/ay4eva2006/ai-interview-question-generator.git
cd ai-interview-question-generator
python -m venv venv && source venv/bin/activate
Environment Variables:
Create a .env file and populate:
code
Env
DATABASE_URL=postgresql://user:pass@localhost:5432/db
REDIS_URL=redis://localhost:6379/0
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
OPENROUTER_API_KEY=your_key
Database Migrations:
code
Bash
flask db upgrade
Run Tests:
code
Bash
pytest
🧠 The "Narrowing" Logic (Prompt Engineering)
The application implements a strict Topic Filter at the service layer. Every user input is passed through a "Professional Reality Check" logic that:
Validates input against standardized O*NET/LinkedIn career taxonomies.
Rejects frivolous or non-professional inputs with a standardized [WRONG JOB DESCRIPTION] signal.
Automatically formats the AI output into a clean, unnumbered 3-paragraph structure to prevent UI breakage.
👨‍💻 Author
Ayo John Adekunle
Built with passion for AI, Scalability, and Clean Code.
GitHub: @ay4eva2006
Portfolio: ay4eva2006.me <!-- Replace with your actual portfolio if you have one -->
📄 License
This project is licensed under the MIT License.
