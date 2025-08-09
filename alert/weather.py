import requests 

api="c9d7a5418da4822623950029ce86be5e"
base_url=f"https://api.openweathermap.org/data/2.5/weather?"

def weather(city):
    response = requests.get(base_url + "appid=" + api + "&q=" + city)
    data = response.json()
    main = data['main']
    temperature = main['temp']
    temprature_celcius = round(temperature - 273.15,2)
    pressure = main['pressure']
    humidity = main['humidity']
    weather_description = data['weather'][0]['description']
    print(f"City: {city}")
    print(f"Temperature: {temprature_celcius} Celcius")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")

if __name__ == "__main__":
    weather("Delhi")