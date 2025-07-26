from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory=".")

def get_answer_from_db(question: str):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM chatbot_data WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Sorry, I don't understand that yet."

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/chat", response_class=HTMLResponse)
async def form_post(request: Request, message: str = Form(...)):
    answer = get_answer_from_db(message)
    return templates.TemplateResponse("index.html", {"request": request, "response": answer})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
