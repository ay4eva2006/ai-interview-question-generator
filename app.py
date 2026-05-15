from flask import Flask, render_template
from dotenv import load_dotenv

from config import Config
from models import db
from routes.interview_routes import interview_bp
from extensions import limiter

# 1. Load environment variables
load_dotenv()

# 2. Create Flask app
app = Flask(__name__)

# 3. Load config first (This sets up the DB and Redis URLs)
app.config.from_object(Config)

# 4. Initialize extensions
db.init_app(app)
limiter.init_app(app)

# 5. Register blueprints
app.register_blueprint(interview_bp)

# 6. Routes
@app.route("/")
def home():
    return render_template("index.html")

# 7. Create database tables
with app.app_context():
    db.create_all()

# 8. Run app (Render/Docker will use Gunicorn, but this is for local)
if __name__ == "__main__":
    # Host 0.0.0.0 is required for Docker
    app.run(host="0.0.0.0", port=10000)