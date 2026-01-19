
from fastapi import FastAPI, UploadFile, File
import shutil, os
from stt import transcribe_audio
from rag import build_vector_store, get_answer

app = FastAPI(title="AI Call Intelligence System")

VECTOR_DB = None

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    global VECTOR_DB
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)
    VECTOR_DB = build_vector_store(transcript)

    return {"message": "Audio processed successfully", "transcript": transcript}


@app.post("/ask")
async def ask_question(question: str):
    if VECTOR_DB is None:
        return {"error": "Please upload an audio file first."}
    answer = get_answer(VECTOR_DB, question)
    return {"answer": answer}
