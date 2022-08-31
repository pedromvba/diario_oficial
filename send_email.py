import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv


# Email server parameters
PORT = 465
EMAIL_SERVER = 'smtp.gmail.com'

# Loading environmental variables

folder_dir = Path('__file_').resolve().parent # __file = path of this file; .resolve = absolut path;
                                              # .parent = path of the parent folder

env_dir = folder_dir/'.env'
load_dotenv(env_dir)

# Reading environmental variables

sender_email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')








































# import smtplib
# from email.message import EmailMessage
#
# msg = EmailMessage()
#
# my_address ="pedro.dataanalysis@gmail.com"    #sender address
#
# app_generated_password = "hpuxwfqqtxrxmsif"    # gmail generated password
#
# msg["Subject"] ="The Email Subject"   #email subject
#
# msg["From"]= my_address      #sender address
#
# msg["To"] = "pedromvba@gmail.com"     #reciver address
#
# msg.set_content("This is the body of the email")   #message body
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#
#     smtp.login(my_address,app_generated_password)    #login gmail account
#
#     print("sending mail")
#     smtp.send_message(msg)   #send message
#     print("mail has sent")