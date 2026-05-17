import re


def validate_job_title(job_title: str):
    if not job_title:
        return "Job title is required"

    job_title = job_title.strip()

    if len(job_title) < 2:
        return "Please enter a valid job title"

    if job_title.isdigit():
        return "Please enter a valid job title"

    if re.fullmatch(r"[a-zA-Z]{1,2}", job_title):
        return "Please enter a more descriptive job title"

    return None


def normalize_job_title(job_title: str) -> str:
    if not job_title:
        return ""

    job_title = job_title.strip()
    job_title = re.sub(r"\s+", " ", job_title)

    return job_title.title()