import json
json_response = """
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
"""
response = json.loads(json_response)
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

    print(response_body)