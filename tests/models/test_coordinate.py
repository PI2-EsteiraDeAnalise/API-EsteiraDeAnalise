from models.coordinate import Coordinate

def test_new_coordinate():
    """
    GIVEN a Coordinate model
    WHEN a new Coordinate is created
    THEN check if the tag and coordinates fields are defined correctly
    """
    coordinate = Coordinate("sample_tag", { "x1": 0, "y1": 10, "x2": 10, "y2": 10 })
    assert coordinate.tag == "sample_tag"
    assert coordinate.coordinates == { "x1": 0, "y1": 10, "x2": 10, "y2": 10 } 
