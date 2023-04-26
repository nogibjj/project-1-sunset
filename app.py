from flask import Flask, render_template, request
import requests
# import json
import datetime
# from datetime import date
import pytz
import collections
from geo import get_location
from imageLinks import srcOfSunsetImages

def sun_rise_set(timezone_name: str, latitude: str, longitude: str, dateInput:str):
    response = requests.get('https://api.sunrise-sunset.org/json', params={'lat': latitude, 'lng': longitude, 'date': dateInput}).json()
    tz = pytz.timezone(timezone_name)
    time_zone = tz.utcoffset(dt=datetime.datetime.utcnow())
    sunrise = datetime.datetime.strptime(response['results']['sunrise'], "%I:%M:%S %p")
    sunset = datetime.datetime.strptime(response['results']['sunset'], "%I:%M:%S %p")
    dawn = datetime.datetime.strptime(response['results']['civil_twilight_begin'], "%I:%M:%S %p")
    dusk = datetime.datetime.strptime(response['results']['civil_twilight_end'], "%I:%M:%S %p")
    solar_noon = datetime.datetime.strptime(response['results']['solar_noon'], "%I:%M:%S %p")
    result = collections.OrderedDict()
    result = {'sunrise': str((sunrise + time_zone).time()), 
              'sunset': str((sunset + time_zone).time()),
              'day length': response['results']['day_length'],
              'solar noon': str((solar_noon + time_zone).time()),
              'dawn begin': str((dawn + time_zone).time()),
              'dusk end': str((dusk + time_zone).time()),
              'lat': latitude,
              'lng': longitude,
              'time zone': timezone_name,
              'date': dateInput,
    }
    return result


def add(x,y):
    return x+y
    
app = Flask(__name__)

# @app.route("/")
# def home():
#     # return render_template(('hello.html', name = name))
#     return 'Welcome to the Sunset Info'

# @app.route("/")
# def index():
#     title = "Homepage"	
#     # return render_template("index.html", title=title, location = get_location(), temperature = get_temperature(), city_info = get_city_info())

# @app.route("/get-weather", methods=['POST'])
# def get_weather():
# 	if request.method == 'POST':
# 		data = request.json
# 		location = get_location(data['city'])
# 		return {'temperature': get_temperature(location), 'wiki': get_city_info(data['city'])}

@app.route('/', methods=["GET", "POST"])
def get_time():
    
    if request.method == 'POST':
        address = request.form['address']
    else:
        address = "Duke University"

    date_ = datetime.date.today()
    
    geo_info = get_location(address)
    
    lat = str(geo_info['lat'])
    lng = str(geo_info['lng'])
    timezone = geo_info['timezone']
    
    date_ = str(date_)
    
    result = sun_rise_set(timezone, lat, lng, date_)
    result['address'] = address
    
    return render_template('sunset.html', data = result, imageSrc = srcOfSunsetImages[0])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
