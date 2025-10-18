from flask import Blueprint, jsonify, request, session
import random

math_captcha_bp = Blueprint("math_captcha", __name__)


# Function to generate a random math question
def generate_math_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-"])  # Extendable to *, /

    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Calculate the answer

    session["math_captcha_answer"] = answer  # Store answer in session
    return question


# API Endpoint to generate Math CAPTCHA
@math_captcha_bp.route('/generate_math_captcha', methods=['GET'])
def generate_math_captcha_api():
    question = generate_math_captcha()
    return jsonify({"question": question})


# API Endpoint to verify Math CAPTCHA
@math_captcha_bp.route('/verify_math_captcha', methods=['POST'])
def verify_math_captcha():
    data = request.json
    user_answer = int(data.get("answer"))
    correct_answer = session.get("math_captcha_answer")

    if user_answer == correct_answer:
        return jsonify({"success": True, "message": "✅ Correct answer!"}), 200
    return jsonify({"success": False, "message": "❌ Incorrect answer, try again!"}), 400
