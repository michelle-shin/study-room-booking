import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms

def main():
    with open('data/rooms.json') as fp:
        data = json.load(fp)  
    BCIT = Rooms()
    for index in range(len(data)):
        room_number = data[index]["room_number"]
        room = Room(room_number)
        for inside_index in range(len(data[index]["availability"])):
            available = data[index]["availability"][inside_index]["available"]
            time_slot = data[index]["availability"][inside_index]["time_slot"]
            booked_by = data[index]["availability"][inside_index]["booked_by"]
            room.add_availability(Availability(time_slot, available, booked_by))
        BCIT.add_room(room)
    
    print(BCIT.to_json_list())

if __name__ == "__main__":
    main()