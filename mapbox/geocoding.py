import requests
import json
import keys

YOUR_MAPBOX_ACCESS_TOKEN = keys.API_key
# provide list of addresses here
address_list = ['kigamboni']

for ADDRESS_TO_SEARCH in address_list:
    endpoint = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{ADDRESS_TO_SEARCH}.json?country=tz&proximity=-73.990593%2C40.740121&access_token={YOUR_MAPBOX_ACCESS_TOKEN}"
    json_response = requests.get(endpoint)
    response = json.loads(json_response.text)
    geo_coordinate_features = response.get("features")
    for feature in geo_coordinate_features:
        place_name = feature.get("place_name")
        place_geometry = feature.get("geometry")
        coordinates = place_geometry.get("coordinates")
        place_type = feature.get("place_type", False)

    boundary = [0,0,0,0]
    center = [0,0]

    if place_type:
        if place_type[0] != "locality":
            boundary = feature.get("bbox")
            center = feature.get("center")

    # print place name, longitude, latitude
    response_body = {
        "place_name": place_name, 
        "longitude" : coordinates[0], 
        "latitude" : coordinates[1],
        "bbox_center" : center,
        "boundary_square_matrix" : boundary
    }

    print(f"{ADDRESS_TO_SEARCH}\n", response_body)
