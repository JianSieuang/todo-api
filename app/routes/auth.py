import os
from flask import Blueprint, redirect, url_for, session, jsonify
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.google import make_google_blueprint, google

auth_bp = Blueprint("auth", __name__)

github_bp = make_github_blueprint(
    client_id=os.getenv("GITHUB_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_OAUTH_CLIENT_SECRET")
)

google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
)

auth_bp.register_blueprint(github_bp, url_prefix="/github_login")
auth_bp.register_blueprint(google_bp, url_prefix="/google_login")

@auth_bp.route('/login')
def login():
    return '''
        <div class="container" style="text-align: center; margin-top: 50px;">
            <a href="/auth/github_login">Login with GitHub</a>
            <a href="/auth/google_login">Login with Google</a>
        </div>
    '''

@auth_bp.route('/github_login')
def github_login():
    
    if not github.authorized:
        return redirect(url_for("auth.github.login"))
    account_info = github.get("/user")
    return jsonify(account_info.json())

@auth_bp.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for("auth.google.login"))
    account_info = google.get("/oauth2/v1/userinfo")
    return jsonify(account_info.json())