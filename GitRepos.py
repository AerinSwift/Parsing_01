import requests, json

url = 'https://api.github.com'
user='AerinSwift'

repos = requests.get(f'{url}/users/{user}/repos')

with open('repos.json', 'w') as file_data:
    json.dump(repos.json(), file_data)


for i in repos.json():
    print(i['name'])
