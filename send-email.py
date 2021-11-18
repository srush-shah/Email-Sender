# Package: smtplib
# Concept: sending a request to the server

import smtplib

from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Your name'
email['to'] = 'Receiver\'s email id here'
email['subject'] = 'Email subject'
email.set_content('Content of the email')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo() #server object

    smtp.starttls() #used to send data between server and client
    smtp.login('Your email id','Your password') #login id and password of your gmail
    smtp.send_message(email)

print('Email Sent')