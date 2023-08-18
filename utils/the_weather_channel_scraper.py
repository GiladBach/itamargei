
import requests
from consts import the_weather_channel_url as url, headers
from bs4 import BeautifulSoup


def run_weather_channel_scraper():
    res = {}
    page = requests.get(url, headers=headers)
    if page.status_code == 404:
        print(url + ' couldnt be found')
    else:
        soup = BeautifulSoup(page.text, 'html.parser')

        high_temp, low_temp, cond = get_low_high_temp_cond(soup)

        sunrise, sunset = get_sunrise_sunset(soup)

        res['high_temp'] = high_temp
        res['low_temp'] = low_temp
        res['sunrise'] = sunrise
        res['sunset'] = sunset
        res['condition'] = cond

        return res

def get_sunrise_sunset(soup):
    try:
        result = soup.find_all('div', attrs={'class': 'TwcSunChart--datesContainer--3MzoF'})[0]
        ps = result.find_all('p')
        return ps[0].text, ps[1].text
        return 1, 1
    except Exception as e:
        print(e)

def get_low_high_temp_cond(soup):
    results = soup.find_all('div', attrs={'class': 'CurrentConditions--tempHiLoValue--3T1DG'}, limit=1)
    conditions = soup.find_all('div', attrs={'class': 'CurrentConditions--phraseValue--mZC_p'})[0].text
    return [x.text for x in results[0].find_all('span', attrs={'data-testid': 'TemperatureValue'})] + [conditions]


    # for item in [x.text for x in results]:
    #     if '/' in item:
    #         print(item)
    #         return item.split('/')