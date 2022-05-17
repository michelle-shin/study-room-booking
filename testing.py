import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from cryptography.fernet import Fernet
from models.users import Users

def main():
    cred = Credentials()
    users = Users()


if __name__ == "__main__":
    main()