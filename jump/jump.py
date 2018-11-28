import requests

url = 'https://den.jumpbikes.com/opendata/free_bike_status.json'
res = requests.get(url)
print(res.status_code)
print(res.json())
