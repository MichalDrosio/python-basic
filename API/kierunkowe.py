import requests

url ='https://www.orange.pl/portal/map/map/article?id=2707635'

r = requests.get(url)
print(r.status_code)

response_dict = r.json()


