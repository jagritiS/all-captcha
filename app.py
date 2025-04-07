from flask import Flask
from text_captcha import text_captcha_bp
from math_captcha import math_captcha_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Register the blueprints
app.register_blueprint(text_captcha_bp)
app.register_blueprint(math_captcha_bp)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

