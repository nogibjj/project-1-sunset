from app import sun_rise_set

test_answer = {
  "date": "2023-02-01", 
  "dawn begin": "06:49:23", 
  "day length": "10:28:49", 
  "dusk end": "18:09:16", 
  "lat": "36.00015569999999", 
  "lng": "-78.94422972195878", 
  "solar noon": "12:29:19", 
  "sunrise": "07:14:55", 
  "sunset": "17:43:44", 
  "time zone": "America/New_York"
}

def test_change():
    assert test_answer == sun_rise_set("America/New_York", '36.00015569999999', '-78.94422972195878','2023-02-01')