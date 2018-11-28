import requests
import pandas as pd

url = 'https://gbfs.bcycle.com/bcycle_denver/station_information.json'
res = requests.get(url)

stations = res.json()['data']['stations']
station_dict = {k: [] for k in stations[0]}

for station in stations:
    for k, v in station.items():
        station_dict[k].append(v)

df = pd.DataFrame(station_dict)
df.to_csv('./bcycle/stations.csv', index=False)
