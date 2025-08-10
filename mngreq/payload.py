
import requests

payload = {'hello': 'world'} # this will send the data to the server
payload1 = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload) # this will get the data from the server 
print(r.url)