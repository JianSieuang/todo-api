def test_github_login(client):
    response = client.get("/auth/github_login/github")
    assert response.status_code in [302, 200]

def test_google_login(client):
    response = client.get("/auth/google_login/google")
    assert response.status_code in [302, 200]
