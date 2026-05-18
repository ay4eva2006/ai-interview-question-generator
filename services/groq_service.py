import os

from openai import OpenAI

from services.prompt_builder import build_interview_prompt


def get_groq_client():

    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        print("GROQ API KEY NOT FOUND")
        return None

    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )


GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant"
]


def generate_groq_questions(job_title):

    client = get_groq_client()

    if not client:
        return None

    prompt = build_interview_prompt(job_title)

    for model in GROQ_MODELS:

        try:

            print(f"[GROQ] Trying model: {model}")

            response = client.chat.completions.create(

                model=model,

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert technical interviewer. "
                            "Generate clear and professional interview questions."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7,
                max_tokens=500
            )

            content = response.choices[0].message.content

            if not content:
                print(f"[GROQ] Empty response from {model}")
                continue

            print(f"[GROQ] Success using {model}")

            return content.strip()

        except Exception as e:

            print(f"[GROQ ERROR - {model}]:", e)

            continue

    print("[GROQ] All models failed")

    return None