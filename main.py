import datetime

from utils.the_weather_channel_scraper import run_weather_channel_scraper
from utils.moon_phases_scraper import run_moon_phases_scraper
from utils.time_genie_scraper import run_genie_time_scraper

def main():
    main_dict = {}
    weather_channel_dict = run_weather_channel_scraper()
    time_genie_dict = run_genie_time_scraper()

    moon_phases_dict = run_moon_phases_scraper()

    main_dict = {
                    **weather_channel_dict,
                    **time_genie_dict,
                    **moon_phases_dict,
                    'date': datetime.datetime.now().strftime("%d/%m/%Y"),
                 }

    print(main_dict)

if __name__ == '__main__':
    main()
