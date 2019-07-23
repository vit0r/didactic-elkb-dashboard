from requests import get, post
from sys import argv

*_, req_number = argv

response = post('http://localhost:5000/data/', {'ok':True})
print(f"response code flaskapp {response.status_code}\n")
if response.status_code != 200:
  raise ValueError('Unload flask app')

for i in range(1, int(req_number)):
    print(f"request number: {i}\n")
    response = get('http://localhost:3000/')
    print(f"response code nginx {response.status_code}\n")
