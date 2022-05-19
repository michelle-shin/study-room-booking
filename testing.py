import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from cryptography.fernet import Fernet
from models.users import Users
from models.email import Email

def main():

    mail = Email()
    # mail.send_booking_confirmation("A01283117", "555", "8:00 - 9:00")
    mail.send_password("A01283112")

if __name__ == "__main__":
    main()