import smtplib
import ssl
from email.message import EmailMessage


def send_notification_email(email, msg):
    """
    Send  email notification to the specified email address.

    Args:
        email (str): email address to send the notification to.
        balance (float): balance to include in the notification email.
    """

    email_sender = '#'
    email_password = '#'
    email_receiver = email
    subject = 'Update from Stock Market '
    body = f"{msg}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
