import os
from flask import Blueprint, redirect, url_for, session, jsonify
from flask_dance.contrib.github import make_github_blueprint, github

auth_bp = Blueprint("auth", __name__)

github_bp = make_github_blueprint(
    client_id=os.getenv("GITHUB_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_OAUTH_CLIENT_SECRET")
)

@auth_bp.route('/login')
def login():
    return '''
        <a href="/auth/github_login">Login with GitHub</a>
    '''
auth_bp.register_blueprint(github_bp, url_prefix="/github_login")

@auth_bp.route('/github_login')
def github_login():
    
    if not github.authorized:
        return redirect(url_for("auth.github.login"))
    account_info = github.get("/user")
    # session['username'] = account_info.json()["login"]
    return jsonify(account_info.json())