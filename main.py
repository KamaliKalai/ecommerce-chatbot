from fastapi import FastAPI
from pydantic import BaseModel
from database import get_answer_from_db

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    answer = get_answer_from_db(user_message)
    return {"response": answer}
