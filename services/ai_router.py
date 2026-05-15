from services.gemini_service import generate_ai_questions

from services.groq_service import generate_groq_questions

from services.openrouter_service import generate_openrouter_questions



def generate_questions(job_title):

    # TRY GEMINI
    questions = generate_ai_questions(job_title)

    if questions:

        print("Using Gemini")

        return questions

    # TRY GROQ
    questions = generate_groq_questions(job_title) 
    
    if questions:
        
        print("print groq")
        
        return questions

    # TRY OPENROUTER
    questions = generate_openrouter_questions(job_title)

    if questions:

        print("Using OpenRouter")

        return questions

    # FINAL FALLBACK
    print("Using local fallback questions")

    return """
1. Tell me about yourself.

2. Describe a difficult technical challenge.

3. How do you handle deadlines?
"""