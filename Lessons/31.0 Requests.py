import requests

response = requests.get("https://www.vinebedding.com")
print(response.status_code)

for key, value in response.headers.items():
    print(key, value)
print("--------------------")
for key, value in response.cookies.items():
    print(key, value)
