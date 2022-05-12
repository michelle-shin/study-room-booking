import pytest
from models.rooms import Rooms

def test_get_time_slots():
    path = '../data/sam.json'
    BCIT = Rooms(path)
    assert set(BCIT.get_time_slots()) == {"11:00 - 12:00", "15:00 - 16:00", "16:00 - 17:00"}

def test_cancel_booking():
    path = '../data/sam.json'
    BCIT = Rooms(path)
    room_number = "558"
    time_slot = "12:00 - 13:00"
    id = "A01283117"
    BCIT.get_room(room_number).cancel_booking(id, time_slot)
    assert BCIT.get_room(room_number).get_availibility(time_slot)["available"]=="Yes"