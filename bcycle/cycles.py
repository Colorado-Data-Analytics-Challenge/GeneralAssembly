import requests
import pandas as pd

url = 'https://gbfs.bcycle.com/bcycle_denver/station_status.json'
res = requests.get(url)

cycles = res.json()['data']['stations']
cycle_dict = {k: [] for k in cycles[0]}

for cycle in cycles:
    for k, v in cycle.items():
        cycle_dict[k].append(v)

df = pd.DataFrame(cycle_dict)
df.to_csv('./bcycle/cycles.csv', index=False)
