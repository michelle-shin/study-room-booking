from models.room import Room
from models.availability import Availability
import json

class Rooms():
    def __init__(self, data):

        self.rooms_list = []

        for index in range(len(data)):
            room_number = data[index]["room_number"]
            room = Room(room_number)
            for inside_index in range(len(data[index]["availability"])):
                available = data[index]["availability"][inside_index]["available"]
                time_slot = data[index]["availability"][inside_index]["time_slot"]
                booked_by = data[index]["availability"][inside_index]["booked_by"]
                room.add_availability(Availability(time_slot, available, booked_by))
            self.rooms_list.append(room)

    def get_room_numbers(self):
        rooms = []
        for room in self.rooms_list:
            rooms.append(room.number)
        return rooms

    def get_room(self, room_number):
        for room in self.rooms_list:
            if room.number == room_number:
                return room
        return None

    def get_room_availability(self, room_number):
        for room in self.rooms_list:
            if room.number == room_number:
                return room.availability
        return None

    def to_json_list(self):
        json_list = []
        for room in self.rooms_list:
            json_list.append(room.get_room_bookings())
        return json_list

    def save_to_json(self):
        with open("data/rooms.json", "w") as outfile:
            json.dump(self.to_json_list(), outfile)
