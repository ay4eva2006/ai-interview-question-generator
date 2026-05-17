import os
from openai import OpenAI

def get_groq_client():
    # Ensure this is your GROQ key (starts with gsk_)
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return None
    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )

def generate_groq_questions(job_title):
    client = get_groq_client()
    if not client:
        print("GROQ ERROR: No API Key found")
        return None

    # We move the rules to the system role for better "Strict" adherence
    system_prompt = "You are an expert recruiter. You provide exactly 3 interview questions without any introductory or concluding text like. You do not use labels like 'Technical' or 'Behavioral'."
    
    user_prompt = f"""Generate exactly 3 professional interview questions for a {job_title} role. 
    Requirements:
    - 2 Technical questions (hard skills/scenarios).
    - 1 Behavioral question (soft skills/past experience).
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7, # Adds a bit of variety to questions
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        print("GROQ ERROR:", e)
        return None