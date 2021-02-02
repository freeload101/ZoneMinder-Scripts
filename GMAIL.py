import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
import datetime

import time
ts = time.time()


smtpUser = 'XXXXXXXXX@gmail.com'
smtpPass = 'XXXXX'

toAdd = 'XXXXXX@gmail.com'
fromAdd = smtpUser

today = datetime.date.today()

subject  = '%s' % datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
header = 'To :' + toAdd + '\n' + 'From : ' + fromAdd + '\n' + 'Subject : ' + subject + '\n'
body = '%s' % datetime.datetime.fromtimestamp(ts).strftime('%H:%M%p %Y-%m-%d')

#attach = '/tmp/tmp.jpg'
attach = '/tmp/tmp.mp4'
#attach = 'Data on %s.csv' % today.strftime('%Y-%m-%d')

print header


def sendMail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = smtpUser
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(smtpUser,smtpPass)
    server.sendmail(smtpUser, to, msg.as_string())

    print 'Done'

    server.quit()


sendMail( ["XXXXXX@gmail.com"], subject, body, [attach] )
sendMail( ["XXXXXXX@gmail.com"], subject, body, [attach] )

