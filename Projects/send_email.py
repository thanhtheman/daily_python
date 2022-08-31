from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib
load_dotenv()

email_sender = 'thanhb.quach@gmail.com'
email_password = os.getenv("GMAIL_PASSWORD")
email_receiver ='thanh.ecommerce2021@gmail.com'

subject = 'Sending email with Python'
body = "You can learn how to send email with Python on FreeCodeCamp. It's easy!"

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())