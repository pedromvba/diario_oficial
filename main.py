'''
Program to...
'''

from datetime import date
from send_email import send_email

import gspread
import pandas as pd


# Connecting to Google Sheet

service_account = gspread.service_account(filename='partnerships-due-dates-4ff6e6fd5095.json')
sheet = service_account.open('Partnerships Due Dates')

# Selecting the work sheet inside the file
work_sheet = sheet.worksheet('Test Database')

# Imports the data as a data frame
df = pd.DataFrame(work_sheet.get_all_records())

# Converts string to datetime type, coerce forces it even if the values are null or empty
df['Data do Lembrete'] = pd.to_datetime(df['Data do Lembrete'], format='%d/%m/%Y', errors='coerce')

# Function to Query the Data and Send E-mail

def due_dates_and_email(dataframe):
   present = date.today()
   email_counter = 0
   for _, row in dataframe.iterrows():
      if (present >= row['Data do Lembrete'].date()) and (row['Fiscal Informado'].lower() == 'no'):
         send_email( subject= f"Due Date Reminder of {row['Parceiro']}", name = row['Fiscal Titular'], receiver_email='pedromvba@gmail.com', due_date = row['Vencimento'], partnership = row['Parceiro'], e_process= row['Processo SIGA'])
         email_counter += 1
   return f'Total e-mails sent{email_counter}'

result = due_dates_and_email(df)

print(result)












#if__name__=='__main__':
