##########################################################################
# sendmail.py
# Vince Dinh, APO Fall 2022
# Script to automate emails for rushees. Can be repurposed for other excomm 
# members.
# Reference:
# https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/
##########################################################################
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import schedule
import time

# Mail stuff. Can modify subject and text vars to repurpose
# App password needed to login: https://support.google.com/accounts/answer/185833
# When running script, enter recipients as new arguments
# EX: python3 sendmail.py joe@gmail.com slug@ucsc.edu
def mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login('pledgemasteremail@gmail.com', 'App Password')

    subject = 'Thank you for your participation!'
    text = 'Hello,\n\nThank you for your interest in our Brotherhood and participating in rush for Fall 2022. We are pleased to let you know that you have met eligibility to pledge. If you choose to attend Bid Night tomorrow (Wednesday, Sept. 28), you may have the chance to begin the process of becoming a part of our fraternity. Should we expect your attendance? More details will be given in the case you choose to accept our invitation.' 

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    msg['From'] = 'Pledge Master <pledgemasteremail@gmail.com>'

    # to = []
    to = sys.argv[1:]
    print(to)
    smtp.sendmail(from_addr='pledgemasteremail@gmail.com',
                to_addrs=to, msg=msg.as_string())
    smtp.quit()

mail()
# Shoots a new email every day at 10pm as long as script is running
# Just make sure to comment out call to mail above first
# schedule.every().day.at("22:00").do(mail)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
