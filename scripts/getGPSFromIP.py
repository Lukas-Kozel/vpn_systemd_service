import requests

keyPath = "key"
ip_address = "147.228.128.15"

with open(file=keyPath,mode="r") as file:
    APIKey = file.read()

url = f"http://api.ipstack.com/{ip_address}?access_key={APIKey}"
response = requests.get(url=url)
data = response.json()

print(data['latitude'])
print(data['longitude'])