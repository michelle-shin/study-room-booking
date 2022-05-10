from flask import Flask, jsonify, render_template, request
import json
from models.rooms import Rooms

app = Flask(__name__)

@app.route('/', methods=["GET","POST"]) 
def homepage(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book("A01283117", time_slot)
            BCIT.save_to_json()
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room), booked_succesfuly="True"), 200
        elif request.method == 'POST' and room_number is not None and room_number!="":
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number)), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    except:
        return "", 400

@app.route('/home', methods=["GET","POST"]) 
def home(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book("A01283117", time_slot)
            BCIT.save_to_json()
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
        elif request.method == 'POST' and room_number is not None:
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number)), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    except:
        return "", 400

@app.route('/rooms', methods=["GET","POST"]) 
def room(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book("A01283117", time_slot)
            BCIT.save_to_json()
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room), booked_succesfuly="True"), 200
        elif request.method == 'POST' and room_number is not None:
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number)), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    except:
        return "", 400

@app.route('/timeslots', methods=["GET","POST"]) 
def timeslot(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        time_slot = request.form.get('timeslot')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            print(room, time_slot)
            BCIT.get_room(room).book("A01283117", time_slot)
            BCIT.save_to_json()
            return render_template('timeslot_rooms.html', rooms=BCIT.get_rooms_with_timeslot(time_slot), time_slot=time_slot), 200
        if time_slot is not None:
            return render_template('timeslot_rooms.html', rooms=BCIT.get_rooms_with_timeslot(time_slot), time_slot=time_slot), 200
        else:
            return render_template('timeslot.html', timeslots=BCIT.get_time_slots()), 200
    except:
        return "", 400

@app.route('/view_bookings', methods=["GET","POST"]) 
def view_booking(): 
    id = "A01283117"
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).cancel_booking(id, time_slot)
            BCIT.save_to_json()
        return render_template('view_bookings.html', bookings=BCIT.get_booked_rooms(id)), 200    
    except:
        return "Not able to load view_bookings", 400

if __name__ == "__main__":
    app.run(debug=True)