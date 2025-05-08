import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://admin:admin@db:5432/todos")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GITHUB_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_OAUTH_CLIENT_SECRET")

    GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    OAUTHLIB_INSECURE_TRANSPORT = 1