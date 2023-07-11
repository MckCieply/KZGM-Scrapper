import requests
from bs4 import BeautifulSoup

#Establish connection and scrape rows
def scrapper_innit():
    URL = "https://platformazakupowa.pl/pn/kzgm_katowice/proceedings"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html.parser')

    table = soup.find('table', {"class":"table table-hover"})
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    return rows

#check how much rows does it contain
def count_of_proceedings():
    rows = scrapper_innit() 
    return len(rows)

#create list of active proceedings
def names_of_proceedings():
    proceedings = []
    rows = scrapper_innit()
    for row in rows:
        cells = row.find_all('td')
        name = cells[1].text
        proceedings.append(name+"\n")
    return proceedings

