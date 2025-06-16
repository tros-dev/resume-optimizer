def analyze_resume_content(content: bytes) -> dict:
    # Placeholder logic for ML analysis
    text = content.decode("utf-8", errors="ignore")

    summary = "Detected resume content with 80% match to Data Scientist role."
    score = 0.8
    keywords = ["Python", "Machine Learning", "FastAPI"]

    return {
        "summary": summary,
        "score": score,
        "keywords": keywords
    }
