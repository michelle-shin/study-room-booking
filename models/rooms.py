from models.room import Room
from models.availability import Availability
import json

class Rooms():
    def __init__(self, path):

        with open(path) as fp:
            data = json.load(fp)
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

    #returns a list of all room numbers
    def get_room_numbers(self):
        rooms = []
        for room in self.rooms_list:
            rooms.append(room.number)
        return rooms

    #returns a room object as per given room number
    def get_room(self, room_number):
        for room in self.rooms_list:
            if room.number == room_number:
                return room
        return None

    #returns availability of the given room number
    def get_room_availability(self, room_number):
        for room in self.rooms_list:
            if room.number == room_number:
                return room.availability
        return None

    #returns a list of unbooked time slots
    def get_time_slots(self):
        available_slots = []
        for room in self.rooms_list:
            for availability in room.availability:
                if availability["available"]=="Yes":
                    available_slots.append(availability["time_slot"])
        available_slots = list(set(available_slots))
        available_slots.sort()

        if '9:00 - 10:00' in available_slots:
            available_slots.remove('9:00 - 10:00')
            available_slots.insert(0, '9:00 - 10:00')
        if '8:00 - 9:00' in available_slots:
            available_slots.remove('8:00 - 9:00')
            available_slots.insert(0, '8:00 - 9:00')

        return available_slots

    #returns a list of rooms as per given timeslot
    def get_rooms_with_timeslot(self, time_slot):
        rooms = []
        for room in self.rooms_list:
            for availability in room.availability:
                if availability["available"]=="Yes" and availability["time_slot"]==time_slot:
                    rooms.append(room)
        return rooms

    #returns a list of booked rooms as per given student id
    def get_booked_rooms(self, student_id):
        rooms = []
        for room in self.rooms_list:
            for availability in room.availability:
                if availability["available"]=="No" and availability["booked_by"]==student_id:
                    rooms.append([room.number, availability["time_slot"]])
        return rooms

    def get_all_booked_rooms(self):
        booked_rooms = []
        for room in self.rooms_list:
            for availibility in room.availability:
                booked_by = availibility["booked_by"]
                timeslot = availibility["time_slot"]
                if availibility["available"]=="No":
                    booked_rooms.append([room.number, booked_by, timeslot])
        return booked_rooms

    def clear_all_bookings(self):
        for room in self.rooms_list:
            for availibility in room.availability:
                if availibility["available"]=="No":
                    availibility["available"]="Yes"
                    availibility["booked_by"]=""

    def to_json_list(self):
        json_list = []
        for room in self.rooms_list:
            json_list.append(room.get_room_bookings())
        return json_list

    def save_to_json(self):
        with open("data/rooms.json", "w") as outfile:
            json.dump(self.to_json_list(), outfile)

