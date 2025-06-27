import requests

url = "http://127.0.0.1:8000/items/"
data = {
    "name": "Book",
    "price": 19.99
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())