import smtplib
import os

gmail = os.environ.get('gmail')
password = os.environ.get('gpass')


smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(gmail, password)
smtpobj.sendmail("nsharma0619@gmail.com", "nsharma0619@gmail.com", "Subject : HELLO\n\n\nhello janvi and saloni")

smtpobj.quit()
