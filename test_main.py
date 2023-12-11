import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sentiment tonality analyzer"}

def test_analyze_sentiment():
    data = {"text": "This is a test sentence."}
    response = client.post("/analyze_sentiment", json=data)
    assert response.status_code == 200
    assert "label" in response.json()
    assert "score" in response.json()

