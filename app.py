from fastapi import FastAPI
from model import calculate_similarity

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Analyzer API"}

@app.post("/analyze")
def analyze(data: dict):
    resume = data["resume"]
    job_desc = data["job_description"]

    score = calculate_similarity(resume, job_desc)

    return {
        "match_score": round(score * 100, 2)
    }