import requests

endpoint = "http://127.0.0.1:8000/apka/update/2"

get_response = requests.get(endpoint)
print(get_response.json())
