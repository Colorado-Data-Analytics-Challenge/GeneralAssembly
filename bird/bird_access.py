import requests
# import pandas as pd

url = "https://api.bird.co/user/login"
data = '{"email": "shane.mcguckian@gmail.com"}'
headers = {
    "Device-Id": "0CC333A5-DC48-4BA8-8F68-B9FA58CE4B21",
    "Platform": "ios",
    "Content-Type": "application/json",
    # "App-Version": "3.0.5",
    }
res = requests.post(url, data=data, headers=headers)
print(res.status_code)
print(res.content)
