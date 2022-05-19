import yagmail
from models.users import Users
from models.credentials import Credentials

class Email():
    def __init__(self):
        self.yag = yagmail.SMTP("email.studyroombooking@gmail.com")
        self.users = Users()
        self.credentials = Credentials()

    def send_password(self, id):
        receiver = self.users.get_email_from_id(id)
        name = self.users.get_name_from_id(id)
        password = self.credentials.get_password_from_id(id)
        receiver = "goutamthukral@gmail.com"
        subject = "Password for Study Room Booking Webapp"
        body = "Hi "+ name +"! Your password is "+ password
        self.send_email(receiver, subject, body)

    def send_account_acceptance_confirmation(self, id):
        receiver = self.users.get_email_from_id(id)
        receiver = "goutamthukral@gmail.com"
        subject = "Account approved by administrator"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your account has been approved by administrator."
        self.send_email(receiver, subject, body)

    def send_cancelling_confirmation(self, id, room, time_slot):
        receiver = self.users.get_email_from_id(id)
        receiver = "goutamthukral@gmail.com"
        subject = "Booked room cancelled"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your booking for room "+ room +" for slot "+ time_slot +" has been cancelled by administrator."
        self.send_email(receiver, subject, body)

    def send_booking_confirmation(self, id, room, time_slot):
        receiver = self.users.get_email_from_id(id)
        receiver = "goutamthukral@gmail.com"
        subject = "Room Booked confirmation"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your booking for room "+ room +" for slot "+ time_slot +" has been confirmed."
        self.send_email(receiver, subject, body)

    def send_email(self, email, subject, message):
        self.yag.send(        
            to=email,
            subject=subject,
            contents=message
        )