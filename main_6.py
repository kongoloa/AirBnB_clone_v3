#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ Get amenity_id with name Wifi
    """
    r = requests.get("http://0.0.0.0:5000/api/v1/amenities")
    print("1")
    r_j = r.json()
    print('2')
    amenity_id = None
    for amenity_j in r_j:
        if amenity_j.get('name') == "Wifi":
            print("we set that shit")
            amenity_id = amenity_j.get('id')
            break
    print(amenity_id)
    # Only Wifi
    
    """ POST /api/v1/places_search
    """
    r = requests.post("http://0.0.0.0:5000/api/v1/places_search", data=json.dumps({ 'amenities': [amenity_id] }), headers={ 'Content-Type': "application/json" })
    print(type(r))
    print(r)
    print("3")
    r_j = r.json()
    print("4")
    print(len(r_j))
