from flask import Blueprint, jsonify, request, session
import random

slider_captcha_bp = Blueprint("slider_captcha", __name__)

@slider_captcha_bp.route('/generate_slider_captcha', methods=['GET'])
def generate_slider_captcha():
    # Random target position for the puzzle piece (simulate backend logic)
    target_position = random.randint(100, 250)
    session['slider_target'] = target_position
    print(target_position)
    return jsonify({"target_position": target_position})  # Only for debugging, remove in production

@slider_captcha_bp.route('/verify_slider_captcha', methods=['POST'])
def verify_slider_captcha():
    data = request.json
    user_position = int(data.get("slider_value"))
    target_position = session.get('slider_target')
    print(user_position, target_position)
    print(target_position)
    # Allow a small margin of error
    if abs(user_position - target_position) <= 5:
        return jsonify({"success": True, "message": "✅ Verified!"})
    else:
        return jsonify({"success": False, "message": "❌ Try Again!"})
