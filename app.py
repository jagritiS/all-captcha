from flask import Flask, jsonify, send_file, session
from captcha.image import ImageCaptcha
import random
import string
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"


# Function to generate random text
def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# API Endpoint to generate CAPTCHA
@app.route('/generate_captcha', methods=['GET'])
def generate_captcha():
    captcha_text = generate_captcha_text()
    image = ImageCaptcha(width=280, height=90)
    image_path = f"static/{captcha_text}.png"
    image.write(captcha_text, image_path)

    session['captcha_text'] = captcha_text  # Store CAPTCHA in session

    return jsonify({
        "captcha_text": captcha_text,  # (Optional: For testing, remove in production)
        "captcha_url": f"/static/{captcha_text}.png"
    })


# API Endpoint to verify CAPTCHA
@app.route('/verify_captcha/<user_input>', methods=['GET'])
def verify_captcha(user_input):
    if user_input == session.get('captcha_text'):
        return jsonify({"message": "✅ CAPTCHA Verified!"}), 200
    return jsonify({"message": "❌ Incorrect CAPTCHA"}), 400


# Serve CAPTCHA images
@app.route('/static/<filename>')
def serve_captcha(filename):
    return send_file(f"static/{filename}")


if __name__ == '__main__':
    app.run(debug=True)
