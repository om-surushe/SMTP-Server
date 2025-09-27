#!/usr/bin/env python3
"""
Script to send a demo email through Gmail SMTP.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def send_email():
    # Load environment variables
    load_dotenv('.env.local')
    
    # Email configuration
    sender = os.getenv('SMTP_USERNAME')
    recipient = 'omsurushe1907@gmail.com'
    subject = 'SMTP Server Demo Email'
    
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    
    # Create the body of the message (a plain-text and an HTML version)
    text = """\
    Hello,
    
    This is a test email sent from the SMTP server demo.
    
    If you can read this, the SMTP server is working correctly!
    
    Best regards,
    SMTP Server Demo
    """
    
    html = """\
    <html>
      <head></head>
      <body>
        <h2>Hello,</h2>
        <p>This is a <strong>test email</strong> sent from the SMTP server demo.</p>
        <p>If you can read this, the SMTP server is working correctly!</p>
        <p>Best regards,<br>SMTP Server Demo</p>
      </body>
    </html>
    """
    
    # Record the MIME types of both parts - text/plain and text/html
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    # Attach parts into message container
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT'))) as server:
            # Login to the SMTP server
            server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
            
            # Send the email
            server.send_message(msg)
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    send_email()
