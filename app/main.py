from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Resume Optimizer API is running"}

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    # Placeholder: add ML logic here
    return {"filename": file.filename, "summary": "ML analysis would go here"}
