import requests
from bs4 import BeautifulSoup
import sqlite3 as sql

#Check how much proceedings is active
def active_proceedings():
    URL = "https://platformazakupowa.pl/pn/kzgm_katowice/proceedings"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html.parser')

    table = soup.find('table', {"class":"table table-hover"})

active_proceedings()