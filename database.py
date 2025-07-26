import json
from difflib import get_close_matches

with open("ecommerce_dataset.json", "r") as file:
    dataset = json.load(file)

def get_answer_from_db(user_message):
    questions = [item["question"] for item in dataset]
    matches = get_close_matches(user_message.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)

    if matches:
        matched_question = next(q for q in questions if q.lower() == matches[0])
        for item in dataset:
            if item["question"] == matched_question:
                return item["answer"]
    return "Sorry, I don't understand that yet."


