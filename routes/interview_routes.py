from flask import Blueprint, request, jsonify
from services.ai_router import generate_questions
from utils.validators import validate_job_title

from models import db
from models.interview import Interview
from models.analytics import Analytics
from extensions import limiter
import json

interview_bp = Blueprint(
    "interview_bp",
    __name__
)

@interview_bp.route("/generate", methods=["POST"])
@limiter.limit("3 per minute")
def generate():

    data = request.get_json()

    job_title = data.get("job_title", "").strip()

    error = validate_job_title(job_title)
    if error:
        return jsonify({"error": error}), 400

    questions = generate_questions(job_title)

    if not questions:
        return jsonify({
            "error": "Failed to generate questions"
        }), 500

    new_interview = Interview(
        role=job_title,
        questions=json.dumps(questions)
    )

    analytics = Analytics(
        searched_role=job_title
    )

    try:
        db.session.add(new_interview)
        db.session.add(analytics)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    return jsonify({

    "success": True,

    "questions": questions,

    #"count": 3,

    "role": job_title

}), 200