import pandas as pd
import requests

url = 'https://gbfs.bcycle.com/bcycle_denver/station_status.json'
res = requests.get(url)

cycles = res.json()['data']['stations']
cycle_dict = {k: [] for k in cycles[0]}

for cycle in cycles:
    for k, v in cycle.items():
        cycle_dict[k].append(v)

old_cycles = pd.read_csv('./bcycle/cycles.csv')
new_cycles = pd.DataFrame(cycle_dict)
all_cycles = pd.concat([old_cycles, new_cycles], axis=0)
all_cycles.to_csv('./bcycle/cycles.csv', index=False)
