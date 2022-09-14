'''
Program to...
'''

from datetime import date
from send_email import send_email

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# Connecting to Google Sheet

service_account = gspread.service_account(filename='partnerships-due-dates-4ff6e6fd5095.json')
sheet = service_account.open('Partnerships Due Dates')

# Selecting the work sheet inside the file
work_sheet = sheet.worksheet('Test Database')

# Imports the data as a data frame
df = pd.DataFrame(work_sheet.get_all_records())

# Converts string to datetime type, coerce forces it even if the values are null or empty
df['Data do Lembrete'] = pd.to_datetime(df['Data do Lembrete'], format='%d/%m/%Y', errors='coerce')






#if__name__=='__main__':
