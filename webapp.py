from flask import Flask, jsonify, render_template, request
import json
from models.rooms import Rooms

app = Flask(__name__)

@app.route('/', methods=["GET","POST"]) 
def homepage(): 
    with open('data/rooms.json') as fp:
        data = json.load(fp)
    BCIT = Rooms(data)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book("A01283117", time_slot)
            BCIT.save_to_json()
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room)), 200
        elif request.method == 'POST' and room_number is not None and room_number!="":
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number)), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    except:
        return "", 400

@app.route('/home', methods=["GET","POST"]) 
def home(): 
    with open('data/rooms.json') as fp:
        data = json.load(fp)
    BCIT = Rooms(data)
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

@app.route('/room', methods=["GET","POST"]) 
def room(): 
    with open('data/rooms.json') as fp:
        data = json.load(fp)
    BCIT = Rooms(data)
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

if __name__ == "__main__":
    app.run(debug=True)