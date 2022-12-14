
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def exchangerate_api_request(currency):
    '''
    Requests to exchangerate-api
    currency must be a string of three capital letters: e.g. EUR
    '''
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(currency)
    res = requests.get(url)
    return res
    

def foursquare_request_venues_authorized(request, latitude, longitude, myquery, radius = 1000, limit=1):
    '''
    Requests to foursquare-api:
    Input:
    request: string:
    1) 'search': Returns a list of venues near the current location, matching a search term.
    2) 'explore': Returns a list of recommended venues near the current location.
    ll = '40.7243,-74.0018'.
    query = a search term to be applied against venue names: 'coffee'.
    limit = number of results to return, up to 50. Defaults to 1.
    radius = Limit results to venues within this many meters of the specified location. Defaults to 1km.
    '''

    url = 'https://api.foursquare.com/v3/places/{}'.format(request)
    params = {
        #client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
        #client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
        "v":'20180604', # version parameter
        "ll":'{},{}'.format(latitude,longitude),  
        "query": myquery,
        "limit":limit,
        "radius": radius
    }

    headers = {
    "Accept": "application/json",
    "Authorization": "fsq3JejeYY/l2E/dCxlcJ8LDqaJLTjykhEPyTNvwPTenz4c="
    }

    resp = requests.request("GET", url=url, params=params,headers=headers)
    return json.loads(resp.text)


def foursquare_venue_by_categories(request, latitude, longitude, categories, radius = 1000, limit=1):
    '''
    Requests to foursquare-api:
    Input:
    request: string:
    1) 'search': Returns a list of venues near the current location, matching a search term.
    2) 'explore': Returns a list of recommended venues near the current location.
    ll = '40.7243,-74.0018'.
    categories = A comma separated list of categories to limit results to:
    https://developer.foursquare.com/docs/resources/categories
    limit = number of results to return, up to 50. Defaults to 1.
    radius = Limit results to venues within this many meters of the specified location. Defaults to 1km.
    '''
    url = 'https://api.foursquare.com/v3/places/{}'.format(request)
    # params = dict(
    #     #client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
    #     #client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
    #     v='20180604', # version parameter
    #     ll='{},{}'.format(latitude,longitude),
    #     limit=limit,
    #     radius=radius,
    #     categoryId = categories
    # )
    params = {
        #client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
        #client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
        "v":'20180604', # version parameter
        "ll":'{},{}'.format(latitude,longitude),  
        "limit":limit,
        "radius": radius,
        "categoryId" : categories
    }
    headers = {
    "Accept": "application/json",
    "Authorization": "fsq3JejeYY/l2E/dCxlcJ8LDqaJLTjykhEPyTNvwPTenz4c="
    }
    resp = requests.request("GET",url=url, params=params,headers=headers)
    return json.loads(resp.text)


def venuesListByQuery(coords, offices, venue_type, radius):
    aux_list = []
    for i in range(len(coords)):
        data = foursquare_request_venues_authorized('search', coords[i]['coordinates'][1],
                                            coords[i]['coordinates'][0], venue_type,
                                            radius)
        aux_list.append([offices[i],data])
    return aux_list


def venuesListByCategory(coords, offices, categories, radius):
    '''
    Vegan restaurants: '4bf58dd8d48988d1d3941735'
    party places: '4bf58dd8d48988d11f941735'
    Colleges: ['4f4533804b9074f6e4fb0105', '4bf58dd8d48988d13d941735','52e81612bcbc57f1066b7a46','52e81612bcbc57f1066b7a45','4f4533814b9074f6e4fb0107','4f4533814b9074f6e4fb0106']
    '''
    aux_list = []
    for i in range(len(coords)):
        data = foursquare_venue_by_categories('search', coords[i]['coordinates'][1],
                                            coords[i]['coordinates'][0], categories,
                                            radius)
        aux_list.append([offices[i],data])
    return aux_list

