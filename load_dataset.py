import json
import sqlite3

with open("ecommerce_dataset.json", "r") as file:
    data = json.load(file)

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS chatbot_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

for item in data["conversations"]:
    cursor.execute("INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", (item["question"], item["answer"]))

conn.commit()
conn.close()

print("✅ Data inserted successfully!")
