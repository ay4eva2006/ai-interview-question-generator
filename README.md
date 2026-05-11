📌 AI Interview Question Generator

An AI-powered web application that generates interview questions for any job role using Google Gemini AI. Built with Flask, JavaScript, HTML, and CSS.

🚀 Features
Generate interview questions for any job title
Mix of technical and behavioral questions
AI-powered responses using Google Gemini
Clean and simple UI
Real-time results without page reload
🛠️ Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
AI Model: Google Gemini API
Environment Management: Python-dotenv
📷 Preview
Input: Software Engineer  
Output:  
1. Explain OOP principles  
2. What is REST API?  
3. Describe a challenging project...  
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/ay4eva2006/ai-interview-question-generator.git
cd ai-interview-question-generator
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt

If you don’t have requirements.txt, create it:

pip freeze > requirements.txt
4. Add environment variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
5. Run the app
python app.py

Open:

http://127.0.0.1:5000
🔑 API Setup

This project uses Google Gemini API.

Get your API key here:
Google AI Studio

📁 Project Structure
ai-interview-question-generator/
│
├── app.py
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── .env
├── .gitignore
└── README.md
⚠️ Important Notes
Never upload .env or API keys to GitHub
Make sure venv/ is ignored
Use environment variables for security
📈 Future Improvements
Add login system
Save generated questions
Export questions as PDF
Improve AI prompt tuning
Deploy online (Render / Vercel)
👨‍💻 Author

Ayo John Adekunle
GitHub: https://github.com/ay4eva2006
