def generate(self, job_title):

    prompt = build_interview_prompt(job_title)

    # STEP 1: provider fallback (ONLY ONCE)
    response = self.router.invoke(prompt)

    # STEP 2: parse JSON safely
    parsed = AIResponseParser.parse(response.text)

    # STEP 3: retry ONLY if parsing fails
    if "error" in parsed:
        response = self.retry.run(self.router, prompt)
        parsed = AIResponseParser.parse(response.get("raw_output", ""))

    # STEP 4: normalize payload
    parsed = self.normalize_payload(parsed)

    # STEP 5: validate with Pydantic
    try:
        validated = InterviewResponse(**parsed)

    except Exception as e:
        AILogger.log("validation_error", {
            "error": str(e),
            "raw": parsed
        })
        return {"error": "schema_validation_failed"}

    # STEP 6: success log
    AILogger.log("success", {
        "job_title": job_title
    })

    return validated.model_dump()