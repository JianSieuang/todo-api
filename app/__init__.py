from flask import Flask
from config import Config
from app.extensions import db
from app.routes.todos import todos_bp
from app.routes.auth import auth_bp, github_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    app.register_blueprint(todos_bp, url_prefix="/api")

    return app
