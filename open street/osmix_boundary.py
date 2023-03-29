import osmnx as ox


def get_coordinates(place_name):
    try:
        city_boundary = ox.geocode_to_gdf(place_name)
        polygon = city_boundary["geometry"].iloc[0]

        # Print the boundary coordinates
        return polygon.exterior.coords.xy
    except:
        return []
