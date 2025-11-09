import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')

def send_test_email():
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=EMAIL_RECIPIENT,
        subject='✅ AutoFinder24/7 – Test Email',
        html_content="""
        <h2>Połączenie z serwerem AutoFinder24/7 działa poprawnie!</h2>
        <p>Wiadomość wysłana z serwera Render przez SendGrid.</p>
        <p><b>Status:</b> OK ✅</p>
        """
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ Wysłano testowy e-mail! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Błąd wysyłki: {e}")

if __name__ == "__main__":
    send_test_email()
