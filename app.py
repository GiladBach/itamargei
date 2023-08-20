import requests
from flask import Flask, render_template, request, redirect, url_for
from consts import API_KEY as api_key

app = Flask(__name__)

#gets the weather data from api.weatherapi.com
def get_weather_data(city, date):
    base_url = f'http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={date}'
    response = requests.get(base_url)
    data = response.json()
    print(data)
    return data

#gets the prayer times
def get_prayer_times(city, date):
    base_url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=CountryName&date={date}&method=2'
    response = requests.get(base_url)
    data = response.json()
    print(data)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        date = request.form['date']
        # weather_data = get_weather_data(city, date)
        # prayer_times = get_prayer_times(city, date)
        return redirect(url_for('response', city=city, date=date))

    return render_template('index.html')

@app.route('/response/<city>/<date>')
def response(city, date):
    weather_data = get_weather_data(city, date)
    prayer_times = get_prayer_times(city, date)
    return render_template('response.html', weather_data=weather_data, prayer_times=prayer_times)

if __name__ == '__main__':
    app.run(debug=True)