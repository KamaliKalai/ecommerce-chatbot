from database import get_answer_from_db

def get_chatbot_response(user_input):
    response = get_answer_from_db(user_input)
    return response
