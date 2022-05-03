import requests
import json

try:
    resp1 = requests.get('https://comp-3297-studysafe.herokuapp.com/hku-member/')
except requests.exceptions.ConnectionError:
    connected = 0
result = resp1.json()
for i in range(len(result)):
    req_str = "https://comp-3297-studysafe.herokuapp.com/record/" + result[i]["hku_id"]
    resp1 = requests.get(req_str)
    result = resp1.json()
    print(result)