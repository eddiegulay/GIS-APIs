import pytest
import osmix_api

def test_get_coordinates():
    address_name = "tanga, Tanzania"
    boundary_coords = osmix_api.get_coordinates(address_name)
    print("Test passes automatically if coordinates csv file is created")


if __name__ == '__main__':
    pytest.main()


def test_get_distance():
    point1 = (-5.0709, 39.0987)
    point2 = (-5.0709, 39.0987)
    distance = osmix_api.get_distance(point1, point2)
    assert distance == 0

def test_get_road_distance():
    p1_address = "Tanga, Tanzania"
    p2_address = "Mkalamo, Tanzania"
    mode = "drive"
    distance = osmix_api.get_road_distance(p1_address, p2_address, mode)

    assert (distance > 110000 and distance <= 180000)

def test_get_coordinates():
    address_name = "tanga, Tanzania"
    org_coord = (-5.202134, 38.2275548)
    coords = osmix_api.get_coordinates(address_name)
    assert coords == org_coord