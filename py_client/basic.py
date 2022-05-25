import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"Hi", "content": "Hello", "price": "123"})
print(get_response.json())