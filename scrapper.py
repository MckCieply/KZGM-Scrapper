import requests
from bs4 import BeautifulSoup
#URL of page with proceedings of intrest
URL = "https://platformazakupowa.pl/pn/kzgm_katowice/proceedings"

#Establish connection and scrape rows
def scrapper_innit():
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

        #Getting name and proceeding link
        name = cells[1].text
        link = "https://platformazakupowa.pl"+row.find('a')['href']
        
        proceedings.append(name + "|" + link + "\n")
    return proceedings
