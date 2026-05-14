import os
import time

from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_ai_questions(job_title):

    prompt = f"""
    You are a senior HR interviewer.

    Generate exactly 5 interview questions
    for a {job_title} role.

    Requirements:
    - 3 technical questions
    - 2 behavioral questions
    - Keep questions concise
    - Return ONLY numbered questions
    """

    fallback_questions = """
1. Tell me about yourself.
2. What are your strengths?
3. Describe a difficult project you handled.
4. How do you solve technical problems?
5. Why should we hire you?
"""

    # Retry logic
    for i in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            # Success
            if response and response.text:
                return response.text

        except Exception as e:

            error_message = str(e)

            print("GEMINI ERROR:", error_message)

            # Handle quota/rate limit errors
            if "429" in error_message:

                print("Quota exceeded. Using fallback questions.")

                return fallback_questions

            # Retry other temporary failures
            print(f"Retrying... attempt {i + 1}")

            time.sleep(2)

    # Final fallback
    return fallback_questions