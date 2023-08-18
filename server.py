from flask import Flask, render_template, request, redirect, url_for

import datetime

from utils.the_weather_channel_scraper import run_weather_channel_scraper
from utils.moon_phases_scraper import run_moon_phases_scraper
from utils.time_genie_scraper import run_genie_time_scraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        date_input = request.form['date_input']
        return redirect(url_for('response', user_input=user_input, date_input=date_input))
    return render_template('index.html')

@app.route('/response/<user_input>/<date_input>')
def response(user_input, date_input):
    weather_channel_dict = run_weather_channel_scraper()
    time_genie_dict = run_genie_time_scraper()

    main_dict = {
        **weather_channel_dict,
        **time_genie_dict,
        'date': datetime.datetime.now().strftime("%d/%m/%Y"),
    }

    return render_template('response.html', user_input=user_input, date_input=date_input)

if __name__ == '__main__':
    app.run(debug=True)
