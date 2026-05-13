from flask import Blueprint, request, jsonify
from services.gemini_service import generate_ai_questions
from utils.validators import validate_job_title

from models import db
from models.interview import Interview
from models.analytics import Analytics


interview_bp = Blueprint(
    "interview_bp",
    __name__
)


@interview_bp.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    job_title = data.get(
        "job_title",
        ""
    ).strip()

    error = validate_job_title(job_title)

    if error:
        return jsonify({
            "error": error
        }), 400

    questions = generate_ai_questions(job_title)

    new_interview = Interview(
        role=job_title,
        questions=questions
    )

    analytics = Analytics(
        searched_role=job_title
    )

    db.session.add(new_interview)
    db.session.add(analytics)

    db.session.commit()

    return jsonify({
        "questions": questions,
        "count": 5,
        "role": job_title
    })