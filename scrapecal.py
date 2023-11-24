
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import numpy as np
from datetime import datetime
import locale
from dateutil import parser
import pickle
locale.setlocale(locale.LC_ALL, 'de_DE')
req.url
req = requests.get("https://www.ccny.cuny.edu/registrar/fall-2018-academic-calendar")
req.status_code
req.text

soup = BS(req.text, 'html.parser')

soup.title
soup.p
data_rows = [row for row in soup.find_all('tr')]
value_series = [row.find_all('td') for row in data_rows]
value_series = [[cell.get_text().strip() for cell in row.find_all('td')] for row in data_rows]
col_head = ["dates","day_of_the_week",'explanation']
df= pd.DataFrame(dict(zip(col_head,list(zip(*value_series)))))
df = df.replace('', np.NaN)
df = df.dropna()
#df.set_index('dates', inplace=True)
#print(df)


df['start_date'],df['end_date'] = df['dates'].str.split(' –',1).str
df['start_date'] = df['start_date']+ ' 2018'
calendar_dates = list(df['start_date'])
calendar_dates[-1] = calendar_dates[-1].replace("2018",'')
calendar_dates[-1] = calendar_dates[-1].replace(",",'')
df.columns
calendar_desc = list(df['explanation'])





# Integrating Google Calendar API in Python Projects
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\User\Desktop\\client_secret.json',scopes=scopes)
#credentials = flow.run_console()
credentials
pickle.dump(credentials,open('token.pkl','wb'))
credentials = pickle.load(open('token.pkl','rb'))
credentials
service = build('calendar','v3',credentials=credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][0]['id']
print(df.index)
j=0
for date in calendar_dates:
    event_f = parser.parse(date).strftime('%Y-%m-%d')
    event = {
  'summary': calendar_desc[j],
  'description': 'Event',
  'start': {
    'dateTime': event_f+'T09:00:00-07:00',
    'timeZone': 'America/New_York',
  },
  'end': {
    'dateTime': event_f+'T09:00:00-07:00',
    'timeZone': 'America/New_York',
  },
}
    created_calendar = service.events().insert(calendarId=calendar_id,body=event).execute()
    j = j + 1



















