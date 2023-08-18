import requests
from datetime import datetime
from bs4 import BeautifulSoup

from consts import moon_phases_url as unformatted_url, headers

def run_moon_phases_scraper():
    formatted_url = unformatted_url + datetime.now().strftime('%d%m%Y')
    print(formatted_url)
    res = {}
    page = requests.get(formatted_url, headers=headers)
    if page.status_code == 404:
        print(formatted_url + ' couldnt be found')
    else:
        soup = BeautifulSoup(page.text, 'html.parser')
        lis = soup.find_all('li')
        for li in lis:
            if '%' in li.text:
                print(li.text.split(' ')[-1])
                res['moon-light'] = li.text.split(' ')[-1]
                return res