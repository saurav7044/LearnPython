# -*- coding: utf-8 -*-
"""
Weather Temperature by location
"""

import requests


def get_location():
    send_url = 'http://freegeoip.net/json'
    j = requests.get(send_url).json()
    lat = j['latitude']
    lon = j['longitude']
    
    return str(lat),str(lon)

def get_weather():
    ID = 'YOUR_KEY_HERE'
    lat,lon = get_location()
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+ID
    jas = requests.get(url).json()
    print("City :",jas['name']+",", jas['sys']['country'])
    print("Weather :",jas['weather'][0]['description'])
    print("Temprature :",str(float(jas['main']['temp'])-273.15)+'°C')   
    
get_weather()
