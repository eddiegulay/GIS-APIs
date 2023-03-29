# GIS APIs (🌍´◡`🌍)

A collection of maps API from Google maps and Mapbox
(mostly experimental)

## 👌 Available APIs
1. Coordinate Geocoding
- Google Maps
- Map Box

2. Region Boundary
- Open Street Overpass API
- osmnx lib

3. Distance API
- Open Street Map (nx network graph)


### 🗺 Google Maps Geocoding 
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


### 🗺 MapBox GeoCoding
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
@@@ Check response.json to see complete mapbox response @@@

## (●'◡'●) Region Boundaries
Just provide location address name and the method will find all coordinated for that region

### Overpass API
Response From Overpass API is not very reliable and has complex queries as per requirements
(Not satble)

### Osmnx API

from osmnx api call get_coordinates(str:)

```python 
address_name = "Kigamboni, Tanzania"
boundary_coords = get_coordinates(address_name)
boundary_coords : [(long), (lat)]
```

## 📏📐 Map Distance 
Getting distance from one point to another on a map. You can either get linear distance with Haversine Algorithm or get distance by following roads

```python
# define starting and ending points
point1 = (39.275229073736654,-6.819505513688398)
point2 = (39.27989377640603,-6.821308691427461)

# call distance method
distance = get_distance(point1, point2) # for linear distance
road_distance = get_road_distance(point1, point2, "drive") # Following road distance
```