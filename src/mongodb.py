
from pymongo import MongoClient, GEOSPHERE

client = MongoClient("mongodb://localhost:27017/") # Establishing the connection with MongoDB


def connectCollection(database, collection):
    '''
    Get one database and collection from MongoDB
    '''
    db = client[database]
    coll = db[collection]
    return db, coll


def getLocation(longitude,latitude):
    '''
    Returns a GeoJSON object
    '''
    location = {
        'type':'Point',
        'coordinates':[longitude, latitude]
    }
    return location


def getCompaniesNear(longitude, latitude, max_distance_m=2000):
    '''
    Returns all companies close to a certain longitude and latitude.
    Maximum distance defaults to 2km.
    '''
    
    db, coll = connectCollection('bigDataProject','companies_cleaned')
    coll.create_index([("office_1_location", GEOSPHERE)])

    return list(coll.find(
    {"office_1_location":{"$near":{"$geometry":{"type":"Point","coordinates":[longitude,latitude]},
                                   "$maxDistance":max_distance_m}}}))
