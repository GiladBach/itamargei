import requests
from bs4 import BeautifulSoup

from consts import time_genie_url as url, headers

def run_genie_time_scraper():
    res = {}
    page = requests.get(url, headers=headers)
    if page.status_code == 404:
        print(url + ' couldnt be found')
    else:
        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find_all('div', attrs={'class': 'links'}, limit=1)
        res['peger'] = results[0].find_next('span').text
        return res