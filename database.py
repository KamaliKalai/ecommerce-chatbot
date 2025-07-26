import sqlite3

def get_answer_from_db(question):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT answer FROM chatbot_data WHERE question = ?", (question,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return "Sorry, I don't understand that yet."
