import smtplib
import os
from email.message import EmailMessage

gmail = os.environ.get('gmail')
password = os.environ.get('gpass')

msg = EmailMessage()
msg['Subject'] = "Greeting for students"
msg['From'] = "nsharma0619@gmail.com"
msg['To'] = "nsharma0619@gmail.com"
msg.set_content("hello janvi and saloni. How are you??")

# smtpobj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# smtpobj.login(gmail, password)
# smtpobj.sendmail("nsharma0619@gmail.com", "nsharma0619@gmail.com", "Subject : HELLO\n\n\nhello janvi and saloni")
# smtpobj.quit()

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtpobj: # with smtplib.SMTP_SSL("localhost", 1025) as smtpobj: python -m smtpd -c DebuggingServer -n localhost:1025
    smtpobj.login(gmail, password)
    smtpobj.send_message(msg)
    
