from flask import Flask, render_template
from dotenv import load_dotenv

from config import Config
from models import db
from routes.interview_routes import interview_bp


load_dotenv()

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(interview_bp)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()