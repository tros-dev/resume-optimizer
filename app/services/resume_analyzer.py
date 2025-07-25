from app.models.schemas import ResumeAnalysisResponse, SkillSummary

class ResumeAnalyzer:
    def __init__(self):
        pass

    def analyze(self, filename: str, content: bytes) -> ResumeAnalysisResponse:
        skills = [
            SkillSummary(skill="Python", confidence=0.95),
            SkillSummary(skill="FastAPI", confidence=0.88),
        ]
        recommendations = [
            "Add more projects with Python",
            "Include measurable outcomes",
        ]
        summary = "Candidate shows strong Python and FastAPI skills."
        return ResumeAnalysisResponse(
            filename=filename,
            summary=summary,
            skills=skills,
            recommendations=recommendations,
        )
