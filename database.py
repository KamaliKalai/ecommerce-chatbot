import sqlite3
from difflib import get_close_matches

def get_answer_from_db(user_message):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    # Fetch all questions from the database
    cursor.execute("SELECT question, answer FROM chatbot_data")
    data = cursor.fetchall()
    conn.close()

    questions = [row[0] for row in data]
    matches = get_close_matches(user_message.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)

    if matches:
        for question, answer in data:
            if question.lower() == matches[0]:
                return answer

    return "Sorry, I don't understand that yet."
