import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///todos.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GITHUB_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_OAUTH_CLIENT_SECRET")