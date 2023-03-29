import requests
import json

# Define your API key and endpoint
API_KEY = 'your_api_key_here'
ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'

# provide address list
addresses = ['Ubungo Maji', 'Mbezi Louis'] #make sure the address name are valid

# Iterate through the list of addresses and make API request
coordinates = []
for address in addresses:
    # Define the API parameters
    params = {'address': address, 'key': API_KEY}

    # Send the API request
    response = requests.get(ENDPOINT, params=params)

    # Parse the API response
    result = json.loads(response.content.decode())
    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']
    coordinates.append((lat, lng))

# display geo-coords
print(coordinates)