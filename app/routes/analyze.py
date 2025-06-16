from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.resume_analyzer import ResumeAnalyzer
from app.models.schemas import ResumeAnalysisResponse

router = APIRouter()

def get_resume_analyzer():
    return ResumeAnalyzer()

@router.post("/analyze-resume/", response_model=ResumeAnalysisResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    analyzer: ResumeAnalyzer = Depends(get_resume_analyzer),
):
    try:
        content = await file.read()
        result = analyzer.analyze(file.filename, content)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
