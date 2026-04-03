from flask import Flask
from config import Config
from db import init_db
from blueprints.auth import auth_bp
from blueprints.feedback import feedback_bp
from blueprints.api import api_bp

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)