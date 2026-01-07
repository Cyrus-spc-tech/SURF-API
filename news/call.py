import requests 
# import pandas as pd 
import rich 
API="019684471d894dd898639151ae78c8b6"
url="https://newsapi.org/v2/everything?q=Apple&from=2025-08-02&sortBy=popularity&apiKey={}".format(API)

response = requests.get(url)
if response.status_code == 200:
    data=response.json()
    rich.print(data)
else :
    print("Error")