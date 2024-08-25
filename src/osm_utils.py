import requests
from geopy.geocoders import Nominatim

def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_project")
    location = geolocator.geocode(location_name)
    return (location.latitude, location.longitude)

def get_nearby_places(query, location_name):
    latitude, longitude = get_location_coordinates(location_name)
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": query,
        "format": "json",
        "limit": 5,
        "viewbox": f"{longitude-0.05},{latitude+0.05},{longitude+0.05},{latitude-0.05}",
        "bounded": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [{"name": place.get("display_name"), "address": place.get("display_name")} for place in response.json()]
    else:
        return []

