from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.services.resume_analyzer import ResumeAnalyzer


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Resume Optimizer API is running"}

def test_analyze_resume():
    resume_content = b"Experienced Python developer with knowledge in ML and APIs"
    files = {"file": ("resume.txt", resume_content, "text/plain")}

    response = client.post("/analyze-resume/", files=files)
    assert response.status_code == 200
    data = response.json()

    assert data["filename"] == "resume.txt"
    assert "summary" in data
    assert isinstance(data["score"], float)
    assert isinstance(data["keywords"], list)


def test_analyze_basic():
    analyzer = ResumeAnalyzer()
    filename = "dummy.pdf"
    content = b"fake resume content"
    result = analyzer.analyze(filename, content)
    assert result.filename == filename
    assert "Python" in [skill.skill for skill in result.skills]
    assert result.summary != ""
