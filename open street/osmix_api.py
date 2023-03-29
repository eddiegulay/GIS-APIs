import osmnx as ox


def get_coordinates(place_name:str):
    try:
        city_boundary = ox.geocode_to_gdf(place_name)
        polygon = city_boundary["geometry"].iloc[0]

        # Print the boundary coordinates
        return polygon.exterior.coords.xy
    except:
        return []

# get approximate distance with Haversine algorithm
# Returns distance in meters
def get_distance(point1, point2):
    try:
        distance = ox.distance.great_circle_vec(point1[0], point1[1], point2[0], point2[1])
        return distance
    except:
        return -1

# get Actual distance by following roads
# Returns distance in Meters
def get_road_distance(point1, point2, mode:str):
    try:
        # Retrieve the street network for the two points
        p1_address = "Uhuru Street, Dar Es salaam"
        p2_address = "Kariakoo"

        G1 = ox.graph_from_point(p1_address, network_type="drive")
        G2 = ox.graph_from_point(p2_address, network_type="drive")

        # Calculate the distance between the two points by following roads in the street network
        distance = ox.distance.euclidean_dist_vec(G1, point1[1], point1[0], G2, point2[1], point2[0], method='haversine')  
        return distance
    except:
        return -1



point1 = (39.275229073736654,-6.819505513688398)
point2 = (39.27989377640603,-6.821308691427461)

distance = get_distance(point1, point2)
distance_r = get_road_distance(point1, point2, "drive")

print("linear: ", distance)
print("Road: ", distance_r)