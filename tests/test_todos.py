import json

def test_get_todos(client):
    response = client.get("/api/todos/")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_todo(client):
    response = client.post("/api/todos/",
        data=json.dumps({"content": "Test TODO"}),
        content_type="application/json"
    )
    assert response.status_code == 201
    assert response.json["content"] == "Test TODO"

def test_toggle_todo(client):
    response = client.post("/api/todos/",
        data=json.dumps({"content": "Toggle TODO"}),
        content_type="application/json"
    )
    todo_id = response.json["id"]

    response = client.put(f"/api/todos/{todo_id}/toggle-completed")
    assert response.status_code == 200
    assert response.json["completed"] is True

def test_delete_todo(client):
    response = client.post("/api/todos/",
        data=json.dumps({"content": "Delete TODO"}),
        content_type="application/json"
    )
    todo_id = response.json["id"]

    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Todo deleted"