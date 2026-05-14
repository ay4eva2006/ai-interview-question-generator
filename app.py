from flask import Flask, render_template
from dotenv import load_dotenv

from config import Config
from models import db
from routes.interview_routes import interview_bp

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Load config
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(interview_bp)


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Create database tables
with app.app_context():
    db.create_all()


# Run app
if __name__ == "__main__":
    app.run()