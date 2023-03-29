# GIS APIs

A collection of maps API from Google maps and Mapbox
(mostly experimental)

## Available APIs
1. Coordinate Geocoding
- Google Maps
- Map Box

### Google Maps Geocoding
1. After Creating account and getting API Key
Register it in the code
```python
# Define your API key and endpoint
API_KEY = 'your_api_key_here'
```
2. Add Address names to places you want to get geo coordinates
```python
# provide address list
addresses = ['Ubungo Maji', 'Mbezi Louis']
```
3. Code response list(longitude, latitude)
```python
lat = result['results'][0]['geometry']['location']['lat']
lng = result['results'][0]['geometry']['location']['lng']
```

### MapBox GeoCoding
1. After Creating Account and getting public key
```c++
// api_key looks like
* pk.eyJ1IjoiZWRkaWVndWxsZWQiLCJhIj......
```

2. Add YOUR_MAPBOX_ACCESS_TOKEN 
```python
# add access token here
YOUR_MAPBOX_ACCESS_TOKEN = keys.API_key
```

3. Add Address names to places you want to get geo coordinates
```python
# provide list of addresses here
address_list = ['kigamboni']
```

4. Output definition
```python
response_body = {
    "place_name": place_name, 
    "longitude" : coordinates[0], 
    "latitude" : coordinates[1],
    "bbox_center" : center,
    "boundary_square_matrix" : boundary
}
```

### Complete Mapbox geo coordinate response
```json
{
    "type": "FeatureCollection",
    "query": ["dar", "es", "salaam", "ubungo"],
    "features": [
      {
        "id": "locality.7482088",
        "type": "Feature",
        "place_type": ["locality"],
        "relevance": 1,
        "properties": {"mapbox_id": "dXJuOm1ieHBsYzpjaXJv"},
        "text": "Ubungo",
        "place_name": "Ubungo, Dar es Salaam, Dar es Salaam, Tanzania",
        "center": [39.209661093, -6.793623225],
        "geometry": {
          "type": "Point",
          "coordinates": [39.209661093, -6.793623225]
        },
        "context": [
          {
            "id": "place.10472",
            "wikidata": "Q1960",
            "mapbox_id": "dXJuOm1ieHBsYzpLT2c",
            "text": "Dar es Salaam"
          },
          {
            "id": "region.247016",
            "short_code": "TZ-02",
            "wikidata": "Q557539",
            "mapbox_id": "dXJuOm1ieHBsYzpBOFRv",
            "text": "Dar es Salaam"
          },
          {
            "id": "country.8936",
            "short_code": "tz",
            "wikidata": "Q924",
            "mapbox_id": "dXJuOm1ieHBsYzpJdWc",
            "text": "Tanzania"
          }
        ]
      },
      {
        "id": "place.10472",
        "type": "Feature",
        "place_type": ["place"],
        "relevance": 0.611111,
        "properties": {"wikidata": "Q1960", "mapbox_id": "dXJuOm1ieHBsYzpLT2c"},
        "text": "Dar es Salaam",
        "place_name": "Dar es Salaam, Dar es Salaam, Tanzania",
        "bbox": [39.00716, -7.18748, 39.556805, -6.566258],
        "center": [39.279, -6.818],
        "geometry": {"type": "Point", "coordinates": [39.279, -6.818]},
        "context": [
          {
            "id": "region.247016",
            "short_code": "TZ-02",
            "wikidata": "Q557539",
            "mapbox_id": "dXJuOm1ieHBsYzpBOFRv",
            "text": "Dar es Salaam"
          },
          {
            "id": "country.8936",
            "short_code": "tz",
            "wikidata": "Q924",
            "mapbox_id": "dXJuOm1ieHBsYzpJdWc",
            "text": "Tanzania"
          }
        ]
      },
      {
        "id": "region.247016",
        "type": "Feature",
        "place_type": ["region"],
        "relevance": 0.611111,
        "properties": {
          "short_code": "TZ-02",
          "wikidata": "Q557539",
          "mapbox_id": "dXJuOm1ieHBsYzpBOFRv"
        },
        "text": "Dar es Salaam",
        "place_name": "Dar es Salaam, Tanzania",
        "bbox": [39.00716, -7.2752923, 39.6563725, -6.4710885],
        "center": [39.2803583, -6.8160837],
        "geometry": {"type": "Point", "coordinates": [39.2803583, -6.8160837]},
        "context": [
          {
            "id": "country.8936",
            "short_code": "tz",
            "wikidata": "Q924",
            "mapbox_id": "dXJuOm1ieHBsYzpJdWc",
            "text": "Tanzania"
          }
        ]
      }
    ],
    "attribution": "NOTICE: © 2023 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare."
  }
```
** You can customize response to get all data as per your Requests

---

## Getting Google Map API

1. Create google cloud account
2. In menu open API & services
3. Enable API & services
4. Select Geocoding API
5. Click Enable

## Getting MapBox Access Token
1. [open link]("https://docs.mapbox.com/playground/geocoding/")
2. Create account
3. Go back to playground then copy access token from there 