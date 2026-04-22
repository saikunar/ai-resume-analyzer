# 🚀 AI Resume Analyzer & Job Matcher

> FastAPI-based NLP system that analyzes resumes and returns job match scores in real-time.

---

## 🔥 Features
- Resume vs Job Description matching
- Match score (% output)
- FastAPI-based backend
- Real-time API response
- Ready for deployment

---

## 🧠 Tech Stack
- Python
- FastAPI
- Scikit-learn (TF-IDF, Cosine Similarity)

---

## ⚙️ How It Works
1. Takes resume text and job description  
2. Converts them into numerical vectors using TF-IDF  
3. Computes similarity using cosine similarity  
4. Returns match score  

---

## 📦 API Endpoint

### POST `/analyze`

### 📥 Input
```json
{
  "resume": "your resume text",
  "job_description": "job description text"
}
## 🌐 Live Demo
👉 https://ai-resume-analyzer-xxxx.onrender.com/docs
