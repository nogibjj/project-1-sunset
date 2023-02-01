from flask import Flask
import requests
# import json
import datetime
import pytz
import collections
from geo import get_location

def sun_rise_set(timezone_name: str, latitude: str, longitude: str, date:str):
    response = requests.get('https://api.sunrise-sunset.org/json', params={'lat': latitude, 'lng': longitude, 'date': date}).json()
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
              'date': date,
    }
    return result


app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome to the Sunset Info'
  
# @app.route('/')
# def index():
#     url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
#     r = requests.get(url)
#     j = json.loads(r.text)
#     city = j['city']

#     return city


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

@app.route('/search/<address>/<date>', methods=["GET"])
def get_time(address, date):
    geo_info = get_location(address)
    
    lat = str(geo_info['lat'])
    lng = str(geo_info['lng'])
    timezone = geo_info['timezone']
    
    date = str(date)
    
    result = sun_rise_set(timezone, lat, lng, date)
    result['address you input'] = address
    
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)