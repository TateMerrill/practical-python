import requests
def get_weather_desc_and_temp():
    api_key = "0505751a83b53a0600c6fa19bbb62039"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")

    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
    'temp_min': temp_min,
    'temp_max': temp_max}

def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimun temperature is", weather_dict.get('temp_min'))
    print("The maxium temperature is", weather_dict.get('temp_max'))

main()