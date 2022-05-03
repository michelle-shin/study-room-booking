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
        if request.method == 'POST':
            room_number = request.form.get('room')
            return render_template('room.html', room=BCIT.get_room_data(room_number), number=room_number), 200
        else:
            return render_template('home.html', rooms=BCIT.get_rooms()), 200
    except:
        return "", 400

def get_room_numbers(data):
    room_numbers = []  
    for index in range(len(data)):
        room_number = data[index]["room_number"]
        room_numbers.append(room_number)
    return room_numbers

def get_room_details(data, room_number):
    for index in range(len(data)):
        if room_number == data[index]["room_number"]:
            return 

if __name__ == "__main__":
    app.run(debug=True)