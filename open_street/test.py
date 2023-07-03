import pytest
import osmix_api

def test_get_coordinates():
    address_name = "tanga, Tanzania"
    boundary_coords = osmix_api.get_coordinates(address_name)
    assert len(boundary_coords[0]) == 1
    assert len(boundary_coords[1]) == 1
    assert boundary_coords[0][0] == 39.099912
    assert boundary_coords[1][0] == -94.581213


if __name__ == '__main__':
    pytest.main()