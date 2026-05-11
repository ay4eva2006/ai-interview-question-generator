from flask import Flask, render_template, request, jsonify
from google import genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# FIXED client initialization
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        job_title = data.get("job_title", "").strip()

        # Validation
        if not job_title:
            return jsonify({
                "error": "Job title is required"
            }), 400

        # Minimum length
        if len(job_title) < 4:
            return jsonify({
                "error": "Please enter a valid job title"
            }), 400

        # Must contain letters
        if not any(char.isalpha() for char in job_title):
            return jsonify({
                "error": "Please enter a valid job title"
            }), 400

        # Common valid job keywords
        valid_keywords = [
            "engineer", "developer", "designer", "manager",
            "accountant", "doctor", "nurse", "teacher",
            "analyst", "administrator", "architect",
            "consultant", "officer", "specialist",
            "technician", "scientist", "programmer"
        ]

        if not any(keyword in job_title.lower() for keyword in valid_keywords):
            return jsonify({
                "error": "Please enter a recognizable job title"
            }), 400

        # AI prompt
        prompt = f"""
        You are a senior HR interviewer at a top tech company.
        Generate exactly 5 interview questions for a {job_title} role.

        Requirements:
        - 3 technical questions
        - 2 behavioral questions
        - Keep questions concise (max 20 words each)
        - No explanations
        - Return ONLY a numbered list
        """

        response = None

        # Retry logic
        for i in range(3):
            try:
                response = client.models.generate_content(
                    model="models/gemini-flash-latest",
                    contents=prompt
                )
                break

            except Exception as e:
                print(f"Retrying... attempt {i+1}")
                time.sleep(2)

        if not response:
            return jsonify({
                "error": "AI service is busy. Please try again."
            }), 503

        questions = response.text if response.text else "No response from model"

        return jsonify({
            "questions": questions,
            "count": 5,
            "role": job_title
        })

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "error": "Failed to generate questions. Please try again."
        }), 500
        
        
if __name__ == "__main__":
    app.run(debug=True)