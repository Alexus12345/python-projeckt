import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.oschadbank.ua/currency-rate")

if  response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td",{"class":"heading-block-currency-rate__table-col"})
    res = soup_list[10]
b = float(res.text)
print(b)
    
