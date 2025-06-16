from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeAnalysisRequest(BaseModel):
    filename: str = Field(..., example="resume.pdf")
    content: bytes

class SkillSummary(BaseModel):
    skill: str
    confidence: float = Field(..., ge=0, le=1)

class ResumeAnalysisResponse(BaseModel):
    filename: str
    summary: str
    skills: List[SkillSummary]
    recommendations: Optional[List[str]] = None
