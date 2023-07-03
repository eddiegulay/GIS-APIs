import osmnx as ox
from array import array
import csv


def get_coordinates(place_name:str):
    try:
        location = ox.geocode(place_name)
        return location
    except:
        return ()
        

# get approximate distance with Haversine algorithm
# Returns distance in meters
def get_distance(point1, point2):
    try:
        distance = ox.distance.great_circle_vec(point1[0], point1[1], point2[0], point2[1])
        return distance
    except:
        return -1

# get Actual distance by following roads
def get_road_distance(p1_address:str, p2_address:str, mode:str):
    # try:
        # Retrieve the street network for the two points
    G1 = ox.graph_from_address(p1_address, network_type="drive")
    G2 = ox.graph_from_address(p2_address, network_type="drive")

    # Get the latitude and longitude coordinates of the two points
    point1 = (G1.nodes[list(G1.nodes())[0]]['y'], G1.nodes[list(G1.nodes())[0]]['x'])
    point2 = (G2.nodes[list(G2.nodes())[0]]['y'], G2.nodes[list(G2.nodes())[0]]['x'])

    # Calculate the distance between the two points by following roads in the street network
    distance = ox.distance.euclidean_dist_vec(G1, point1[1], point1[0], G2, point2[1], point2[0], method='haversine')  
    return distance
    # except:
        # return -1


def process_region_boundary(region_name, response):
    coordinates = [(lat, lng) for lat, lng in zip(response[1], response[0])]

    # Define the CSV filename and column headers
    filename = f'{region_name}_coordinates.csv'
    headers = ['latitude', 'longitude']

    # Open the CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the column headers
        writer.writerow(headers)

        # Write each coordinate as a row in the CSV file
        for coord in coordinates:
            writer.writerow(coord)

def geocoord_to_address(lat, lng):
    location = ox.distance.nearest_edges(lat, lng)
    return location