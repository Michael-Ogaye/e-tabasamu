from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(username,email,amount,transact_code,type):
    subject='E-tabasamu wallet'
    mail_content=render_to_string('emails/transact.html',{'username':username,'amount':amount,'trcode':transact_code,'type':type})
    alt_content=render_to_string('emails/transact.txt',{'username':username,'amount':amount,'trcode':transact_code,'type':type})
    sender='michaelogaye87@gmail.com'
    msg=EmailMultiAlternatives(subject,alt_content,sender,[email])
    msg.attach_alternative(mail_content,'text/html')
    msg.send()