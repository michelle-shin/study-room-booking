##ACIT2911 Project - Book Study Space

Study Room Booking Web App

This web app is based on Python Flask and is deployed in Microsoft Azure.
Flask is used to set up a server which accepts requests from end users like students or admins.

#Features of the webapp:

- Signup and Login
- Forgot Password
- To select and book study rooms as per room numbers or timeslots
- View booked rooms
- Real time email notifications
- Admin view to approve the account, and view and cancel all bookings if needed
- Admin password change

All the data for the webapp including booked room details, student details, their encrypted credentials are stored in JSON files.
The data in these files is accessed through various defined classes and methods.

Proper naming conventions are used for classes like Room, Availability, Users.

#Notes:

- flask webapp is in app.py
- templates has all the HTML pages
- static has necessary css and javascript files
- data has all the JSON files to store data
- models has all the classes and methods to access the data

#Running in local directory:

- Clone the repository
- Pip install all the required libraries as per requirements.txt
- Run python app.py

Email service is based upon Logic Apps of Microsoft Azure.
An HTTP request is sent from python server to Logic App which further sends the mail.

The webapp can be accessed from below link
https://studyroombooking.azurewebsites.net/

admin view can be accessed through
https://studyroombooking.azurewebsites.net/admin/login  
login-admin  
password-password

feature to change admin password can be accessed through  
https://studyroombooking.azurewebsites.net/admin/change_password
