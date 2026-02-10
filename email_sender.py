import smtplib
from email.message import EmailMessage
from secrets import sender,receiver,password

# Email details
def send_email(receiver_email: str, subject: str, content: str) -> str:
    """Send an email to the receiver with the given subject and content."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    return {"Email sent successfully to {receiver}!"}