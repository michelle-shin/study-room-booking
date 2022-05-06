import pytest
from models.room import Room
from models.availability import Availability

def test_room():
    room = Room("557")
    assert room.number == "557"

def test_add_availability():
    availability_one = available_one = Availability("11:00 - 12:00", "No", "")
    room = Room("557")
    room.add_availability(availability_one)
    assert len(room.availability) == 1


