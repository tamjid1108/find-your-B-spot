import requests

url = 'https://api.foursquare.com/v3/places/{}'.format('search')

params = {
    #client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
    #client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
    "v":'20180604', # version parameter
    "ll":'{},{}'.format(47.606,-122.349358),  
    "query": 'starbucks',
    "limit":'50',
    "radius":'1000'
}

headers = {
# "Accept": "application/json",
"Authorization": "fsq3JejeYY/l2E/dCxlcJ8LDqaJLTjykhEPyTNvwPTenz4c="
}

resp = requests.request("GET", url=url, params=params,headers=headers)
print(resp.text)