import pytest
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from models.users import Users

def test_get_time_slots():
    path = 'data/sam.json'
    BCIT = Rooms(path)
    assert set(BCIT.get_time_slots()) == {"11:00 - 12:00", "15:00 - 16:00", "16:00 - 17:00"}

def test_if_id_exists():
    users = Users()
    assert users.if_id_exists("A01283117") is True

def test_get_name_from_id():
    users = Users()
    assert users.get_name_from_id("A01283117")=="Goutam Thukral"

def test_room():
    room = Room("557")
    assert room.number == "557"