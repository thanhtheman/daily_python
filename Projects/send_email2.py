from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
import os

load_dotenv()

email_sender ='thanhb.quach@gmail.com'
email_password = os.getenv('GMAIL_PASSWORD')
email_receiver = 'kimmiecorner30@gmail.com'
subject ='Your Awesome Boyfriend - A Phin dep trai'
body = 'Idol tyty dễ thương, giỏi giang, thúng mĩng i love you pặc pặc \n This email is sent with LOVE from a phin by using Python'

email = EmailMessage()

email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())

