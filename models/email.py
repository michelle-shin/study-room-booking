import yagmail
import requests
from models.users import Users
from models.credentials import Credentials

class Email():
    def __init__(self):
        self.yag = yagmail.SMTP("email.studyroombooking@gmail.com")
        self.users = Users()
        self.credentials = Credentials()
        self.url = "https://prod-15.canadacentral.logic.azure.com:443/workflows/d72fb653f1734f0d838a4b96e6239068/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=VeSm7g3ly7vfi4Mja6hPyp1wj_Zy-tPxRQk1MY8y8rI"

    def send_password(self, id):
        receiver = self.users.get_email_from_id(id)
        name = self.users.get_name_from_id(id)
        password = self.credentials.get_password_from_id(id)
        subject = "Password for Study Room Booking Webapp"
        body = "Hi "+ name +"! Your password is "+ password
        self.send_request(receiver, subject, body)

    def send_account_creation_confirmation(self, id):
        receiver = self.users.get_email_from_id(id)
        subject = "Account created in Book Study Space"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your account has been created.\nPlease wait for administrator to approve your account."
        self.send_request(receiver, subject, body)

    def send_account_deletion_confirmation(self, id):
        receiver = self.users.get_email_from_id(id)
        subject = " Book Study Space Account rejected by administrator"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your account request has been rejected by admin.\nPlease contact admin for more information."
        self.send_request(receiver, subject, body)  

    def send_account_acceptance_confirmation(self, id):
        receiver = self.users.get_email_from_id(id)
        subject = "Account approved by administrator"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your account has been approved by administrator."
        self.send_request(receiver, subject, body)

    def send_cancelling_confirmation_admin(self, id, room, time_slot):
        receiver = self.users.get_email_from_id(id)
        subject = "Booked room cancelled by admin"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your booking for room "+ room +" for slot "+ time_slot +" has been cancelled by administrator."
        self.send_request(receiver, subject, body)

    def send_cancelling_confirmation(self, id, room, time_slot):
        receiver = self.users.get_email_from_id(id)
        subject = "Booked room cancelled"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your booking for room "+ room +" for slot "+ time_slot +" has been cancelled."
        self.send_request(receiver, subject, body)

    def send_booking_confirmation(self, id, room, time_slot):
        receiver = self.users.get_email_from_id(id)
        subject = "Room Booked confirmation"
        name = self.users.get_name_from_id(id)
        body = "Hi "+ name +"! Your booking for room "+ room +" for slot "+ time_slot +" has been confirmed."
        self.send_request(receiver, subject, body)

    def send_email(self, email, subject, message):
        self.yag.send(        
            to=email,
            subject=subject,
            contents=message
        )

    def send_request(self, email, subject, message):
        obj = {
            "message":message,
            "email":email,
            "subject":subject
        }
        requests.post(self.url, json = obj)