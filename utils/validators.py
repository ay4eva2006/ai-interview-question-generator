def validate_job_title(job_title):

    if not job_title:
        return "Job title is required"

    if len(job_title) < 4:
        return "Please enter a valid job title"

    if not any(char.isalpha() for char in job_title):
        return "Please enter a valid job title"

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
        return "Please enter a recognizable job title"

    return None