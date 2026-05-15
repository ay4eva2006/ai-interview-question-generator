import time
import logging

from services.gemini_service import generate_ai_questions as gemini
from services.groq_service import generate_groq_questions as groq
from services.openrouter_service import generate_openrouter_questions as openrouter


# CONFIG (easy to manage)
PROVIDERS = [
    ("Gemini", gemini),
    ("Groq", groq),
    ("OpenRouter", openrouter),
]


# VALIDATION
def is_valid_response(response):
    return response and isinstance(response, str) and response.strip()

# ROUTER CORE
def generate_questions(job_title):
    errors = []

    for name, provider in PROVIDERS:
        start_time = time.time()

        try:
            result = provider(job_title)

            latency = round(time.time() - start_time, 2)

            if is_valid_response(result):
                print(f"[AI ROUTER] Using {name} | {latency}s")
                return result
            else:
                print(f"[AI ROUTER] {name} returned invalid response")
                errors.append(f"{name}: invalid response")

        except Exception as e:
            print(f"[AI ROUTER] {name} failed: {e}")
            errors.append(f"{name}: {str(e)}")

    # FINAL FALLBACK
    print("[AI ROUTER] All providers failed. Using fallback.")
    print("Errors:", errors)

    return fallback_questions(job_title)


# SAFE FALLBACK
def fallback_questions(job_title):
    return f"""
1. Tell me about your experience as a {job_title}.
2. What is the most challenging problem you solved?
3. How do you approach learning new technologies?
"""