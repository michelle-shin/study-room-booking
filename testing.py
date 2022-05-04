import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms

def main():
    with open('data/rooms.json') as fp:
        data = json.load(fp)  
    BCIT = Rooms(data)
    for index in range(len(data)):
        room_number = data[index]["room_number"]
        room = Room(room_number)
        for inside_index in range(len(data[index]["availability"])):
            available = data[index]["availability"][inside_index]["available"]
            time_slot = data[index]["availability"][inside_index]["time_slot"]
            booked_by = data[index]["availability"][inside_index]["booked_by"]
            room.add_availability(Availability(time_slot, available, booked_by))
    
    BCIT.get_room("558").book("A01283117", "9:00")

    with open("sample.json", "w") as outfile:
        json.dump(BCIT.to_json_list(), outfile)


if __name__ == "__main__":
    main()