import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.logging_config import configure_logging

logger = configure_logging('notification-service')

# sender_email='notificationmailer77@gmail.com',
# recipient_email='app.devplatform@gmail.com',
# subject='Kafka microservices message',
# message='Hi this is a message sent via kafka',
# smtp_server='smtp.gmail.com',
# smtp_port=587,
# smtp_username='notificationmailer77@gmail.com',
# smtp_password='yhce qtyz vddy rrzf'



def send_email(sender_email, recipient_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    """Send an email notification."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to SMTP server (if authentication is required)
        server.login(smtp_username, smtp_password)

        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(msg)

        # Close connection
        server.quit()
        logger.info(f"Email notification sent to {recipient_email}")
        print(f"Email notification sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email notification: {e}")
        pass

# Example usage:
send_email(sender_email='notificationmailer77@gmail.com',
           recipient_email='app.devplatform@gmail.com',
           subject='Notification Subject',
           message='Notification Message',
           smtp_server='smtp.gmail.com',
           smtp_port=587,
           smtp_username='notificationmailer77@gmail.com',
           smtp_password='yhce qtyz vddy rrzf')

