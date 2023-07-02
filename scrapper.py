import requests
from bs4 import BeautifulSoup

#Check how much proceedings is active
def active_proceedings():
    URL = "https://platformazakupowa.pl/pn/kzgm_katowice/proceedings"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html.parser')

    table = soup.find('table', {"class":"table table-hover"})
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    counter = 0

    for row in rows:
        cells = row.find_all('td')
        name = cells[1].text
        counter += 1
    
    return counter
active_proceedings()