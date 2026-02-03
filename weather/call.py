import requests
import rich
import pandas as pd 

api_key="c9d7a5418da4822623950029ce86be5e"
city= input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response=requests.get(url)

if response.status_code==200:
    data = response.json()
    data=pd.DataFrame(data['main'], index=[0])
    rich.print(data)


else:
    rich.print(f"Error: {response.status_code}")
