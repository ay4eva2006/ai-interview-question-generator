from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

from models import db
from models.interview import Interview
from models.analytics import Analytics

import os
import time

load_dotenv()

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///interviews.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        job_title = data.get(
            "job_title",
            ""
        ).strip()

        # Validation
        if not job_title:

            return jsonify({
                "error":
                "Job title is required"
            }), 400

        if len(job_title) < 4:

            return jsonify({
                "error":
                "Please enter a valid job title"
            }), 400

        if not any(
            char.isalpha()
            for char in job_title
        ):

            return jsonify({
                "error":
                "Please enter a valid job title"
            }), 400

        valid_keywords = [

            "engineer",
            "developer",
            "designer",
            "manager",
            "accountant",
            "doctor",
            "nurse",
            "teacher",
            "analyst",
            "administrator",
            "architect",
            "consultant",
            "officer",
            "specialist",
            "technician",
            "scientist",
            "programmer"

        ]

        if not any(
            keyword in job_title.lower()
            for keyword in valid_keywords
        ):

            return jsonify({
                "error":
                "Please enter a recognizable job title"
            }), 400

        # Prompt
        prompt = f"""
        You are a senior HR interviewer.

        Generate exactly 3 interview
        questions for a {job_title} role.

        Requirements:
        - 2 technical questions
        - 1 behavioral questions
        - concise questions
        - no explanations
        - numbered list only
        """

        response = None

        # Retry logic
        for i in range(3):

            try:

                response = \
                    client.models.generate_content(

                    model="models/gemini-flash-latest",

                    contents=prompt
                )

                break

            except Exception as e:

                print(
                    f"Retrying... attempt {i+1}"
                )

                time.sleep(2)

        if not response:

            return jsonify({
                "error":
                "AI service busy"
            }), 503

        questions = response.text

        # Save interview
        new_interview = Interview(

            role=job_title,

            questions=questions
        )

        db.session.add(new_interview)

        # Save analytics
        analytics = Analytics(

            searched_role=job_title
        )

        db.session.add(analytics)

        db.session.commit()

        return jsonify({

            "questions": questions,

            "count": 3,

            "role": job_title

        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error":
            "Failed to generate questions"
        }), 500


if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)