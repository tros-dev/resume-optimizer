from fastapi import APIRouter, UploadFile, File
from app.models.resume import ResumeAnalysisResult
from app.services.analyzer import analyze_resume_content

router = APIRouter()

@router.post("/analyze-resume/", response_model=ResumeAnalysisResult)
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    analysis = analyze_resume_content(content)
    return ResumeAnalysisResult(
        filename=file.filename,
        **analysis
    )
