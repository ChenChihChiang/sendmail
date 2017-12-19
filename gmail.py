import smtplib
from email.mime.text import MIMEText

def sendmail(from_user, passwd, to_user, subject_msg, body_msg):

    msg = MIMEText(body_msg)
    msg['Subject'] = subject_msg
    msg['From'] = from_user
    msg['To'] = to_user

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(from_user, passwd)
    server.send_message(msg)
    server.quit()

    print('Email sent!')
