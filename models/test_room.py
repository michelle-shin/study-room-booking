import pytest
from models.room import Room
from models.availability import Availability

def test_room():
    room = Room("557")
    assert room.number == "557"

def test_add_availability():
    availability_one = Availability("11:00 - 12:00", "No", "")
    room = Room("557")
    room.add_availability(availability_one)
    assert len(room.availability) == 1

def test_get_room_bookings():
    availability_one = Availability("11:00 - 12:00", "No", "")
    room = Room("557")
    room.add_availability(availability_one)
    bookings = room.get_room_bookings()
    assert bookings["room_number"] == '557'
    assert bookings["availability"][0] == availability_one.to_dict()

def test_book():
    availability_one = Availability("11:00 - 12:00", "No", "")
    room = Room("557")
    room.add_availability(availability_one)
    room.book("A0", "11:00 - 12:00")
    bookings = room.get_room_bookings()
    assert bookings["availability"][0]["booked_by"] == "A0"



