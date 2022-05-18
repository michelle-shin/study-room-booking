from flask import Flask, render_template, request
from models.rooms import Rooms
from models.credentials import Credentials
from models.users import Users

app = Flask(__name__)

@app.route('/', methods=["GET","POST"]) 
def login(): 
    try: 
        return render_template('login.html', methods=['GET','POST'], login="pass"), 200
    except:
        return "", 400

@app.route('/login', methods=["GET","POST"])
@app.route('/home', methods=["GET","POST"]) 
def page():
    path = './data/rooms.json'
    BCIT = Rooms(path)
    id = request.form.get('Username')
    password = request.form.get('Password')
    signup_message = request.form.get('signup')
    if(signup_message=="Sign Up"):
        return render_template('signup.html', methods=['GET','POST']), 200
    credentials = Credentials()
    if(credentials.if_credentials_exist(id, password)):
        return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    else:
        return render_template('login.html', methods=['GET','POST'], id_exists=credentials.if_id_exists(id)), 200

@app.route('/signup', methods=["GET","POST"]) 
def signup():
    id = request.form.get('studentID')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    users = Users()
    cred = Credentials()
    if(users.if_id_exists(id) is True):
        return render_template('signup.html', methods=['GET','POST'], id_exists="yes"), 200
    users.add_new_user(id, name, email)
    cred.save_credentials(id, password)
    users.save_to_json()
    cred.save_to_json(cred.encrypt_credentials())
    try:
        return render_template('login.html', methods=['GET','POST'], id_exists="exists"), 200
    except:
        return "", 400
    
@app.route('/logout', methods=["GET","POST"]) 
def logout():
    try: 
        return render_template('login.html', methods=['GET','POST'], login="pass"), 200
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
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room), booked_succesfuly="True"), 200
        elif request.method == 'POST' and room_number is not None and room_number!="":
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number)), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers()), 200
    except:
        return "", 400

@app.route('/rooms', methods=["GET","POST"]) 
def rooms(): 
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