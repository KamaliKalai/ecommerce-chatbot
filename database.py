import json
from difflib import get_close_matches

with open("ecommerce_dataset.json", "r") as file:
    dataset = json.load(file)

def get_answer_from_db(user_message):
    questions = [item["question"] for item in dataset]
    matches = get_close_matches(user_message.lower(), questions, n=1, cutoff=0.6)
    if matches:
        for item in dataset:
            if item["question"].lower() == matches[0]:
                return item["answer"]
    return "Sorry, I don't understand that yet."
