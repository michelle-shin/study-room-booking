Study Room Booking Web App

This web app is based on Python Flask and is deployed in Microsoft Azure.
Flask is used to set up a server which accepts requests from end users like students or admins.

Main use of the app is to select and book study rooms as per room numbers or timeslots.
All the data for the webapp including booked room details, student details, their encrypted credentials are stored in JSON files.
The data in these files is accessed through various defined classes and methods.

Proper naming conventions are used for classes like Room, Availability, Users.

Flask webapp is in app.py
testing.py file was used to test various functions
templates has all the HTML pages
static has necessary css and javascript files
data has all the JSON files to store data
models has all the classes and methods to access the data
