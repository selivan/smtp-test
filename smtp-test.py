#!/usr/bin/env python3

import sys
import os

import smtplib
from email.mime.text import MIMEText

mail_host = 'email-smtp.eu-west-1.amazonaws.com'
mail_port = 465
use_starttls = False
user = 'XXXXXXXXXXXXXXXXXXXX'
password = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
msg = 'Hello! Does it work?'
subj = 'smtp send test'
mail_from = 'no-reply@example.net'
mail_to = ['user@example.net']
# AWS SES test simulator:
# https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mailbox-simulator.html
#mail_to = ['success@simulator.amazonses.com']
#mail_to = ['bounce@simulator.amazonses.com']
#mail_to = ['ooto@simulator.amazonses.com']
#mail_to = ['complaint@simulator.amazonses.com']
#mail_to = ['suppressionlist@simulator.amazonses.com']

if __name__ == "__main__":
    message = MIMEText(msg, 'plain')
    message['Subject'] = subj
    message['From'] = mail_from

    print("Message:")
    print(message.as_string())

    print("Trying to send...")
    if use_starttls:
        conn = smtplib.SMTP(host=mail_host, port=mail_port)
        conn.starttls()
    else:
        conn = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
    conn.login(user=user, password=password)
    conn.send_message(from_addr=mail_from, to_addrs=mail_to, msg=message)
