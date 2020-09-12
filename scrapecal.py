
#Your mission is to scrape the cuny fall 2018 academic calendar site using the requests library,
#beautiful soup and pandas, just like in class.
#You should wind up with a pandas data frame where the index column is a python date. 
#There should be a column for "day of the week" with variable lable dow and a column called text with the explanation. 
# cols = date,day_of_the_week,explanation
#Print out this data frame. 
#5 extra credit points if you figure out how to use the google api to programatically add these dates to your google calendar with the request library

import requests
from bs4 import BeautifulSoup as BS
req.url
req = requests.get("https://www.ccny.cuny.edu/registrar/fall-2018-academic-calendar")
req.status_code
req.text

soup = BS(req.text, 'html.parser')
print(soup.prettify)
soup.title
soup.p
all_p = soup.find_all('tr')
