def get_response(user_input):
    if "return" in user_input.lower():
        return "To return a product, go to your orders and click 'Return'."
    elif "refund" in user_input.lower():
        return "Refunds are processed within 3-5 business days."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"
