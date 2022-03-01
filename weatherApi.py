import requests

api_key = 'b8310094bc2fd693d6caa7690335f91d'
city = 'Dallas'

url = "http://www.api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=b8310094bc2fd693d6caa7690335f91d"

r = requests.get(url)
json = r.json()

description = json.get('weather')[0].get('description')
print('Todays forecast is', description)
