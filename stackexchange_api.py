import requests

url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)

for data in response.json()['items']:
    print(data['tags'])
