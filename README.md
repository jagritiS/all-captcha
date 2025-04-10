# CAPTCHA API

This is a simple CAPTCHA API built using Flask that generates and verifies CAPTCHA text using images. It includes two main functionalities:

1. **Generate CAPTCHA**: An endpoint that generates a random CAPTCHA text and returns the image URL.
2. **Verify CAPTCHA**: An endpoint to verify the CAPTCHA text entered by the user.


### Step 1: Install Required Libraries

First, install Python and the necessary dependencies by running:

```bash
pip install -r requirements.txt

```
The required libraries are:

Flask: Web framework for creating the API

captcha: Library for generating CAPTCHA images

flask-cors: Handles cross-origin requests

gunicorn: For deploying the app (optional for production)

## Step 2: Create the CAPTCHA API
The API is defined in app.py. It consists of the following endpoints:

/generate_captcha (GET)
Generates a random CAPTCHA and returns the CAPTCHA text along with the image URL.

Response:

json
Copy
Edit
{
    "captcha_text": "X5P7QK",
    "captcha_url": "/static/X5P7QK.png"
}
/verify_captcha/<user_input> (GET)
Verifies the CAPTCHA entered by the user. It compares the user input to the stored CAPTCHA text in the session.

Response:

json
Copy
Edit
{
    "message": "✅ CAPTCHA Verified!"
}
If the CAPTCHA is incorrect:

json
Copy
Edit
{
    "message": "❌ Incorrect CAPTCHA"
}
/static/<filename> (GET)
Serves the CAPTCHA image file.

## Step 3: Run the Application
To run the application locally, execute the following command:

```bash

python app.py
```
This will start the Flask server on http://127.0.0.1:5000/.

Test the API Locally
Generate CAPTCHA: Open: http://127.0.0.1:5000/generate_captcha Response example:
```
json

{
    "captcha_text": "X5P7QK",
    "captcha_url": "/static/X5P7QK.png"
}
```
Verify CAPTCHA: Open: http://127.0.0.1:5000/verify_captcha/X5P7QK Response example:
```
json

{
    "message": "✅ CAPTCHA Verified!"
}
```

Test the API
🔤 Text CAPTCHA:
http://127.0.0.1:5000/generate_captcha

http://127.0.0.1:5000/verify_captcha/X5P7QK

🧮 Math CAPTCHA:
http://127.0.0.1:5000/math

POST to /verify_math_captcha with answer in JSON.

🧩 Slider CAPTCHA (Demo Page):
Access the HTML frontend at /slider .