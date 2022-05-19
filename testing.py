import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from cryptography.fernet import Fernet
from models.users import Users

def main():
    path = './data/rooms.json'
    BCIT = Rooms(path)
    users = Users()
    booking_details = []
    for booking in BCIT.get_all_booked_rooms():
        booking.append(users.get_name_from_id(booking[1]))
        booking_details.append(booking)
    print(booking_details)

if __name__ == "__main__":
    main()