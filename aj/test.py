import requests

url = 'http://localhost:5000/signup'  # Adjust the port/host if needed

payload = {
    "uuid" : "Marzi",
    "username": "aj",
    "phno": "1234567890",
    "email": "aj@example.com",
    "hash": "somehashedpassword"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())