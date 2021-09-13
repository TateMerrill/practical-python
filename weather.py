import requests

api_key = "0505751a83b53a0600c6fa19bbb62039"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
# print(json)

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)

temp_min = json.get("main").get("temp_min")
print("The minimun temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The maxium temperature is", temp_max)
