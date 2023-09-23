import os
import json
import requests

city = input("Enter your city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=db64454a34564f8d933215616232309&q= {city}"
r = requests.get(url)
weather_dict = json.loads(r.text)
w = weather_dict["current"]["temp_c"]
print(w)
os.system(f"say 'the current weather in {city} is {w} degrees celsius'")