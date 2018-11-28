import requests
import pandas as pd

url = 'https://api.bird.co/bird/nearby?latitude=39.751552&longitude=-105.002959&radius=10000'
headers = {
    "Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjJkMjI4NmFjLTdmODItNDhjNC1hNmEwLWY1Njc0OTcyY2UxYyIsImRldmljZV9pZCI6IjBDQzMzM0E1LURDNDgtNEJBOC04RjY4LUI5RkE1OENFNEIyMSIsImV4cCI6MTU3MzQxMTkzNX0.DLA0c-jpkPM2Yrh2m4pWUehOCo-iuVziWBKYb2mR_6Q",
    "Device-id": "0CC333A5-DC48-4BA8-8F68-B9FA58CE4B21",
    "App-Version": "3.0.5",
    "Location": '{"latitude": 39.751552, "longitude": -105.002959, "altitude": 500, "accuracy": 100, "speed": -1, "heading": -1}',
    }
res = requests.get(url, headers=headers)

scooters = res.json()['birds']
print(scooters)
scoot_dict = {
    'id': [],
    'location': [],
    'code': [],
    'captive': [],
    'battery_level': []
    }

for scoot in scooters:
    for k, v in scoot.items():
        if k == 'location':
            scoot_dict[k].append((v['latitude'], v['longitude']))
        else:
            scoot_dict[k].append(v)

df = pd.DataFrame(scoot_dict)
df.to_csv('scoots.csv', index=False)
