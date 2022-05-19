import pytest
from models.rooms import Rooms
from models.credentials import Credentials
from models.users import Users

def test_get_time_slots():
    path = 'data/sam.json'
    BCIT = Rooms(path)
    assert set(BCIT.get_time_slots()) == {"11:00 - 12:00", "15:00 - 16:00", "16:00 - 17:00"}