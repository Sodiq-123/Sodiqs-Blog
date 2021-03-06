from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# def send_email(subject, message, recipient, mail_type="html"):
#   context = ssl.create_default_context()
#   with smtplib.SMTP_SSL(app.config["MAIL_SERVER"], app.config["MAIL_PORT"], context=context) as server: 
#         server.login(app.config["MAIL_SENDER"], app.config['MAIL_PASSWORD'])
#         msg = MIMEMultipart('alternative')
#         msg['Subject'] = subject
#         msg['From'] = app.config['MAIL_SENDER']
#         msg['To'] = recipient 

#         if mail_type == 'html':
#             msg.attach(MIMEText(message, 'html'))
#         else:
#             msg.attach(MIMEText(message, 'plain'))

#         server.sendmail(app.config['MAIL_SENDER'], recipient, msg.as_string())




def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender='sodiq.agunbiade.4@gmail.com', recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
#     # mail.send(msg)
    