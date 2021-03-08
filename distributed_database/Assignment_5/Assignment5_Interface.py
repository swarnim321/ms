#
# Assignment5 Interface
# Name: 
#

from pymongo import MongoClient
import os
import sys
import json
from math import cos, sin, sqrt, atan2, radians

def DistanceFunction(lat2, lon2, lat1, lon1):
    R = 3959
    pi1 = radians(lat1)
    pi2 = radians(lat2)
    delta_pi = radians(lat2-lat1)
    delta_lambda = radians(lon2-lon1)
    a = (sin(delta_pi/2) * sin(delta_pi/2)) + (cos(pi1) * cos(pi2) * sin(delta_lambda/2) * sin(delta_lambda/2))
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c

    return d

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    businesses = collection.find({'city':{'$regex' : cityToSearch, '$options': "$i"}})
    with open(saveLocation1, "w") as f:
        for business in businesses:
            Name= business['name']
            FullAddress = business['full_address']
            City = business['city']
            State =  business['state']
            f.write(Name.upper() + "$" + FullAddress.upper() + "$" + City.upper() + "$" + State.upper() + "\n")
    #pass

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    businesses = collection.find({'categories':{'$in': categoriesToSearch}}, {'name': 1, 'latitude': 1, 'longitude': 1, 'categories': 1})
    loc_longitude = float(myLocation[1])
    loc_latitude  = float(myLocation[0])
    with open(saveLocation2, "w") as f:
        for business in businesses:
            loc_latitude2 = business['latitude']
            loc_longitude2 = business['longitude']
            Name = business['name']
            d = DistanceFunction(loc_latitude2, loc_longitude2, loc_latitude, loc_longitude)
            if d <= maxDistance:
                f.write(Name.upper() + "\n")


    #pass




