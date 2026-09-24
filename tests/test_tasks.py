from fastapi.testclient import TestClient
from crm_api.main import app

client = TestClient(app)

def test_create_task_returns_201():
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"
    
def test_create_task_without_title_returns_400():
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 400
    
    
def test_get_nonexistent_task_returns_404():
    response = client.get("/tasks/9999")
    assert response.status_code == 404