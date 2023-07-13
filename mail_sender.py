import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
load_dotenv()

def produce_email():
    email_address = os.getenv('SENDER_GMAIL')
    email_password = os.getenv('PASSWORD')
    email_recipiant = os.getenv('TARGET_GMAIL')
    message = "Test content message"

    msg = MIMEText(message)
    msg['Subject'] = "Testing mail 2"
    msg['From'] = email_address
    msg['To'] = email_recipiant

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(email_address, email_password)
       smtp_server.sendmail(email_address, email_recipiant, msg.as_string())
