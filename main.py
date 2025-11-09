from flask import Flask
from test_email import send_test_email

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AutoFinder24/7 is running!"

@app.route("/send")
def send_email():
    send_test_email()
    return "📧 Test email sent successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
