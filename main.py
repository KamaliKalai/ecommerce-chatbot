from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Chatbot API!"}

@app.get("/chat")
def chat_with_bot(message: str):
    response = get_response(message)
    return {"response": response}
