import requests 

r = requests.get("https://api.github.com/events") # this is  GET request which mean it will get the data from the server

data = {'key': 'value'}
rp = requests.post('https://httpbin.org/post', data=data) # this is a POST request which mean it will post the data to the server

rpu= requests.put('https://httpbin.org/put', data=data) # this is a PUT request which mean it will update the data to the server

rpde= requests.delete('https://httpbin.org/delete', data=data) # this is a DELETE request which mean it will delete the data to the server

rphe= requests.head('https://httpbin.org/head', data=data) # this is a HEAD request which mean it will get the headers from the server

rpco= requests.options('https://httpbin.org/options', data=data) # this is a OPTIONS request which mean it will get the options from the server

print(rpco.text)

# print(r.status_code)
# print(r.encoding)

with open("github_events.json", "w", encoding="utf-8") as f:
    f.write(r.text)
