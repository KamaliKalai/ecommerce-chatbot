import json
from difflib import get_close_matches

# Load the dataset
with open("ecommerce_dataset.json", "r") as file:
    dataset = json.load(file)

def get_answer_from_db(user_message):
    questions = [item["question"] for item in dataset]
    matches = get_close_matches(user_message.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)

    if matches:
        # Find the original question that matches (case-sensitive lookup)
        for item in dataset:
            if item["question"].lower() == matches[0]:
                return item["answer"]
    
    return "Sorry, I don't understand that yet."




