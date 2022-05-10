import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms

def main():
    BCIT = Rooms('data/rooms.json')
    
    id = "A01283117"
    rooms = BCIT.get_booked_rooms(id)

    for room in rooms:
        print(room[0], room[1])

if __name__ == "__main__":
    main()