from pydantic import BaseModel

class ResumeAnalysisResult(BaseModel):
    filename: str
    summary: str
    score: float
    keywords: list[str]
