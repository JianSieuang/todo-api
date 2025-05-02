from flask import Flask
from config import Config
from app.extensions import db
from app.routes.todos import todos_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(todos_bp)

    return app