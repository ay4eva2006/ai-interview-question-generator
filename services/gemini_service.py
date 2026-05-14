import os
from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get the API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Create the Client (This replaces genai.configure)
client = genai.Client(api_key=api_key)

def generate_ai_questions(job_title):
    prompt = f"""
    You are a senior HR interviewer.
    Generate exactly 3 interview questions for a {job_title} role.
    2 technical and 1 behavioral.
    Number them.
    """

    try:
        # Use the modern client-based call
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # Return the text content
        return response.text

    except Exception as e:

    error_message = str(e)

    print("GEMINI ERROR:", error_message)

    if "429" in error_message:

        return jsonify({

            "error": "AI service is temporarily busy. Please try again later."

        }), 429

    print(f"Retrying... attempt {i+1}")

    time.sleep(2)