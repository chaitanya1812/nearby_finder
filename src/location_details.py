import requests

response = requests.get('https://nominatim.openstreetmap.org/search', params={
    'q': '1600 Pennsylvania Ave NW, Washington, DC 20500',
    'format': 'json'
})
location = response.json()
print(location)