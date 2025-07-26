import sqlite3
import json

# Connect to SQLite database (or create it)
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS chatbot_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Load dataset
with open("ecommerce_dataset.json", "r") as file:
    data = json.load(file)

# Insert data into table
for item in data["conversations"]:
    question = item["question"]
    answer = item["answer"]
    cursor.execute("INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", (question, answer))

# Save and close
conn.commit()
conn.close()

print("Data inserted successfully!")
