import requests 
import json

r = requests.get("https://www.pexels.com/search/bird/")

try:
    print(json.loads(r.text))
except json.JSONDecodeError as e:
    print(f"Error: {e}")