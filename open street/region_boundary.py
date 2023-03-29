import overpass

# Define the query


# sample queries
query_selection = {
    "boundary" : """
        area[name="Address Name"]->.a;
        rel(area.a)[admin_level=8]->.b;
        map_to_area -> .c;
        rel(area.c)[type=boundary][boundary=administrative][admin_level=8]->.d;
        way(r.rel.d)[boundary=administrative]->.e;
        (.e;>;);
        out meta;
    """,
    "location" : """
        [out:json];
        area[name="Address Name"]->.a;
        node["leisure"="park"](area.a);
        out center;
    """,

    "within_area" : """
        [out:json];
        node(around:500,37.7749,-122.4194)["shop"];
        out;
    """
}

# Execute the query and retrieve the boundary coordinates
api = overpass.API()
query = query_selection.get("within_area")
result = api.Get(query)
coordinates = result.get('features')[0].get('geometry').get('coordinates')[0]

# Print the boundary coordinates
print(coordinates)
