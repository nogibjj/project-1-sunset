from geopy.geocoders import Nominatim
from geopy.geocoders import GeoNames


geolocator = Nominatim(user_agent="Sunset")

from timezonefinder import TimezoneFinder
obj = TimezoneFinder()

def get_location(ville="Durham"):
	location = geolocator.geocode(ville)
	output =  {"lat": location.latitude, "lng": location.longitude, }
	timezone = obj.timezone_at(lng = location.longitude, lat= location.latitude)
	
	return  {"lat": location.latitude, "lng": location.longitude, "timezone": timezone }
