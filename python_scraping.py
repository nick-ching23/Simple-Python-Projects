# Python Scraping Project 

from bs4 import BeautifulSoup as BS
import requests
import pandas as pd 

web_page = requests.get("https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD")
content = BS(web_page.content, "html.parser")

table = content.find_all('table')[0]

rows = table.find_all('tr')

row_list = list()

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)

row_list.pop(0)
row_list.pop()

dataframe = pd.DataFrame(row_list, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
print(dataframe)

dataframe.to_csv('bitcoin_prices.csv',encoding='utf-8')


