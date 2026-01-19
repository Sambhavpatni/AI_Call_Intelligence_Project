
# 🎧 Multilingual AI Call Intelligence Platform

This project is a full-stack AI system that converts call recordings into text and allows users to interact with conversations using AI (RAG).

## 🚀 Features
- Speech-to-text using OpenAI Whisper  
- AI-powered question answering  
- Retrieval Augmented Generation (RAG)  
- FastAPI backend  
- Web frontend interface  

## 🧠 Architecture
Audio → Whisper → Transcript → Chunking → Embeddings → FAISS → LLM → Answer

## 🛠 Tech Stack
Python, FastAPI, Whisper, LangChain, FAISS, OpenAI API, HTML, CSS, JavaScript

## ▶ How to Run
Backend:
```
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:
Open `frontend/index.html` in browser.

## 📌 Example Questions
- What problem did the customer face?
- Summarize the call
- What solution was suggested?

## 📈 Future Improvements
- Multilingual optimization  
- Real-time streaming  
- Kafka integration  
- Speaker diarization  
- Dashboard analytics  
