import requests

BASE = "http://127.0.0.1:5000/"

print("\n", "==" * 50)
data = [{"name": "tuan", "views": 10, "likes": 10},
        {"name": "ha", "views": 20, "likes": 20},
        {"name": "random", "views": 30, "likes": 30}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
