
#Your mission is to scrape the cuny fall 2018 academic calendar site using the requests library,
#beautiful soup and pandas, just like in class.
#You should wind up with a pandas data frame where the index column is a python date. 
#There should be a column for "day of the week" with variable lable dow and a column called text with the explanation. 
# cols = date,day_of_the_week,explanation
#Print out this data frame. 
#5 extra credit points if you figure out how to use the google api to programatically add these dates to your google calendar with the request library

import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'de_DE')
req.url
req = requests.get("https://www.ccny.cuny.edu/registrar/fall-2018-academic-calendar")
req.status_code
req.text

soup = BS(req.text, 'html.parser')
print(soup.prettify)
soup.title
soup.p


data_rows = [row for row in soup.find_all('tr')]
value_series = [row.find_all('td') for row in data_rows]
value_series = [[cell.get_text().strip() for cell in row.find_all('td')] for row in data_rows]
col_head = ["dates","day_of_the_week",'explanation']
df= pd.DataFrame(dict(zip(col_head,list(zip(*value_series)))))
df = df.replace('', np.NaN)
df = df.dropna()
df.set_index('dates', inplace=True)
print(df)



df.to_csv(r'C:\Users\User\Desktop\try1.csv', index = False)
str_dates = list(df['dates'])



str_dates[0].isoformat()











all_p = soup.find_all('p')
len(all_p)
all_tables = soup.find_all('table')
len(all_tables)   
col1 = []
col2 =[]
col3 = []

for rowtag in all_p:
    #row = str(rowtag)
 #   row = row.strip('<p>').strip('</p>').strip('strong>').strip('</')
    print(rowtag.get_text())



