import pytest
from models.availability import Availability

def test_availability():
    available_one = Availability("11:00 - 12:00", "No", "")
    
    assert available_one.time_slot == "11:00 - 12:00"
    assert available_one.available == "No"
    assert available_one.booked_by == ""

def test_invalid_availability_constructor():
    with pytest.raises(TypeError):
        Availability(11, "No", "")

    with pytest.raises(ValueError):
        Availability("8:00 - 9:00", "Maybe", "")


def test_to_dict():
    available_one = Availability("11:00 - 12:00", "No", "")

    assert available_one.to_dict() == {"time_slot": "11:00 - 12:00", "available": "No", "booked_by": ""}

