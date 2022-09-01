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


# Defining the function itself
def send_email(subject, receiver_email, name, due_date, partnership, e_process):
    # Creating the base message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = formataddr(('Pedro Monteiro',f'{sender_email}'))  # shows the Pedro Monteiro as the sender instead
                                                                    # of the email address

    # E-mail body (plain text version)
    msg.set_content(

        f'''\
        Saudações {name}, informo que a vigência da Parceria com {partnership}, processo {e_process} terá fim em {due_date}. 
        Assim sendo, favor iniciar as tratativas internas para a renovação.     
        '''
    )

    # Email body (html version)

    msg.add_alternative(

        f'''\
    <html>
    <body>
        <p>Saudações {name}, informo que a vigência da Parceria com <strong>{partnership}</strong>, processo {e_process} terá fim em <strong>{due_date}</strong>.</p>
        <p>Assim sendo, favor iniciar as tratativas internas para a renovação.</p>
    </body>
    </html>  
        ''',
        subtype = 'html'
    )

    with smtplib.SMTP_SSL(EMAIL_SERVER,PORT) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ =='__main__':
    send_email(subject='Due Date Reminder', name='Daniela', receiver_email='pedromvba@gmail.com', due_date = '01/09/2022', partnership='AMT', e_process='TLB-PRO-2022/487')
