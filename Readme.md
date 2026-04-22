# 🚀 AI Resume Analyzer & Job Matcher

An AI-powered API that analyzes resumes and matches them with job descriptions using NLP techniques.

## 🔥 Features
- Resume vs Job Description matching
- Match score (%)
- FastAPI-based backend
- Real-time API response
- Ready for deployment

## 🧠 Tech Stack
- Python
- FastAPI
- Scikit-learn (TF-IDF, Cosine Similarity)

## ⚙️ How It Works
1. Takes resume text and job description
2. Converts them into numerical vectors using TF-IDF
3. Computes similarity using cosine similarity
4. Returns match score

## 📦 API Endpoint

### POST `/analyze`

**Input:**
```json
{
  "resume": "your resume text",
  "job_description": "job description text"
}
