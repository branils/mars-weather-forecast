import requests


HOST = 'https://api.nasa.gov'
PATH = '/insight_weather'
KEY = '/?api_key=9uvBPtFjMXQev7EgkOvqeJFjy7pZFwX2yAyFKvUe'
TYPE = '&feedtype=json&ver=1.0'

URL = HOST + PATH + KEY + TYPE


response = requests.get(url=URL) #HTTP request
json_data = response.json() # convert content to the JSON format


#Martian Day: Sol 610
sol = '610 (13 Aug)'


#Season
season = json_data["610"]["Season"] #Decode JSON


#Temperatures in Celisus
av_temp = json_data["610"]["AT"]["av"] #Decode JSON variable
max_temp = json_data["610"]["AT"]["mx"]
min_temp = json_data["610"]["AT"]["mn"]


#Wind Speed in meter per second
av_wind = json_data["610"]["HWS"]["av"]
max_wind = json_data["610"]["HWS"]["mx"]
min_wind = json_data["610"]["HWS"]["mn"]
#print(max_wind)
