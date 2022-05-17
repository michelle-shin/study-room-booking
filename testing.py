import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from cryptography.fernet import Fernet

def main():
    cred = Credentials()

    encrypted = cred.encrypt_credentials()
    print(encrypted)

if __name__ == "__main__":
    main()