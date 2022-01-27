import logging
import smtplib
import sys
import configparser
from requests import get
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Setup properties file and logger
p = configparser.RawConfigParser()
p.read('project.properties')
logging.basicConfig(filename=p.get('p', 'log_file'),
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout)) # Set logger to output to console + file

testing = p.get('p', 'dev_mode')
logging.info('testing=%s', testing)

ip      = get('https://api.ipify.org').content.decode('utf8')
last_ip = open(p.get('p', 'last_ip'), 'r').readline()

if ip != last_ip:
    logging.info('IP has been changed')

    with open(p.get('p', 'last_ip'), 'w') as file:
        file.write(ip)

    site_link = p.get('p', 'site_link')
    mail_content = f'{site_link} \n' \
                   f'The new ip address is: {ip}\n\n\n' \
                   f'This is an automated email, please delete me!\n\n' \
                   f'Thank you :)'

    if testing == 'true':
        r = p.get('TestRecipients', 'recipient')
        recipients = r.split('\n')
    else:
        r = p.get('Recipients', 'recipients')
        recipients = r.split('\n')

    logging.info('recipients=%s', recipients)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()  # enable security
    session.login(p.get('Sender', 'email'),
                  p.get('Sender', 'pass'))

    for recipient in recipients:
        message = MIMEMultipart()
        message['From'] = p.get('Sender', 'email')
        message['To'] = recipient
        message['Subject'] = 'Lukeflix\'s IP address has changed'  # The subject line

        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        text = message.as_string()
        session.sendmail(p.get('Sender', 'email'), recipient, text)

    session.quit()
    logging.info('Emails sent')
else:
    logging.info('IP has NOT been changed')
    logging.info('Emails NOT sent')
