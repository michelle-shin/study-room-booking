import os
from time import time
from flask import Flask, get_flashed_messages, render_template, request, redirect, session, flash, url_for
from models.rooms import Rooms
from models.credentials import Credentials
from models.users import Users
from models.email import Email

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/', methods=["GET","POST"]) 
def webapp(): 
    try: 
        session.clear()
        return redirect("/login")
    except:
        return "", 400

@app.route('/admin/login', methods=["GET","POST"]) 
def admin_login(): 
    try: 
        if len(session)!=0:
            return redirect('/home')
        return render_template('admin_login.html'), 200
    except:
        return "", 400

@app.route('/admin/login-try', methods=["GET","POST"]) 
def admin_login_try(): 
    try: 
        if len(session)!=0:
            return redirect('/home')
        id = request.form.get('Username')
        password = request.form.get('Password')
        credentials = Credentials()
        users = Users()
        if(credentials.if_admin(id, password)):
            session['id'] = id
            session['name'] = 'admin'
            return redirect("/admin")
        else:
            return render_template('admin_login.html', message="wrong"), 200
    except:
        return "", 400

@app.route('/login', methods=["GET","POST"])
def login():
    try:
        messages = get_flashed_messages()
        for message in messages:
            if message=="exists":
                return render_template('login.html', methods=['GET','POST'], id_exists="exists"), 200 
        if len(session)!=0:
            return redirect('/home')   
        return render_template('login.html', methods=['GET','POST'], login="pass"), 200
    except:
        return "", 400

@app.route('/login-try', methods=["GET","POST"]) 
def login_try():
    path = './data/rooms.json'
    BCIT = Rooms(path)
    id = request.form.get('Username')
    password = request.form.get('Password')
    signup_message = request.form.get('signup')
    if len(session)!=0:
        return redirect('/home') 
    if(signup_message=="Sign Up"):
        return redirect("/signup")
    credentials = Credentials()
    users = Users()
    if(users.if_not_approved(id)):
        return render_template('login.html', methods=['GET','POST'], id_exists="not approved"), 200
    elif(credentials.if_credentials_exist(id, password)):
        session['id']=id
        session['name'] = users.get_name_from_id(id)
        return redirect("/home")
    else:
        return render_template('login.html', methods=['GET','POST'], id_exists=credentials.if_id_exists(id)), 200

@app.route('/signup', methods=["GET","POST"]) 
def signup():
    if len(session)!=0:
        return redirect('/home') 
    return render_template('signup.html', methods=['GET','POST']), 200

@app.route('/signup-try', methods=["GET","POST"]) 
def signup_try():
    if len(session)!=0:
        return redirect('/home')
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
    # email = Email()
    # email.send_account_creation_confirmation(id)
    users.save_to_json()
    cred.save_to_json(cred.encrypt_credentials())
    try:
        # return render_template('login.html', methods=['GET','POST'], id_exists="exists"), 200
        flash('exists')
        return redirect(url_for('login'))
    except:
        return "", 400

@app.route('/forgotpassword', methods=["GET","POST"])
def forgot_password():
        return render_template('forgot_password.html'), 200

@app.route('/forgot_password_try', methods=["GET","POST"])
def forgot_password_try():
    users = Users()
    id = request.form.get('Username')
    if(users.if_id_exists(id)):
        email = Email()
        email.send_password(id)
        return redirect('/login')
    else:
        return render_template('forgot_password.html', message="not_exists"), 200

@app.route('/logout', methods=["GET","POST"]) 
def logout():
    try: 
        session.pop('id')
        session.pop('name')
        return redirect('/login')
    except:
        return "", 400

@app.route('/home', methods=["GET","POST"]) 
def home_page(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if len(session)==0:
            return redirect('/login')
        if session['id']=="admin":
            return redirect('/admin')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book(session['id'], time_slot)
            BCIT.save_to_json()
            email = Email()
            email.send_booking_confirmation(session['id'], room, time_slot)             
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room), booked_succesfuly="True", name=session['name']), 200
        elif request.method == 'POST' and room_number is not None and room_number!="":
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number), name=session['name']), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers(), name=session['name']), 200
    except:
        return "", 400

@app.route('/rooms', methods=["GET","POST"]) 
def rooms(): 
    if session['id']=="admin":
        return redirect('/admin')
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        room_number = request.form.get('room')
        if len(session)==0:
            return redirect('/login')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book(session['id'], time_slot)
            BCIT.save_to_json()
            email = Email()
            email.send_booking_confirmation(session['id'], room, time_slot)            
            return render_template('room.html', methods=['GET','POST'], room=room, availabilities=BCIT.get_room_availability(room), booked_succesfuly="True", name=session['name']), 200
        elif request.method == 'POST' and room_number is not None and room_number!="":
            return render_template('room.html', methods=['GET','POST'], room=room_number, availabilities=BCIT.get_room_availability(room_number), name=session['name']), 200
        else:
            return render_template('home.html', methods=['GET','POST'], rooms=BCIT.get_room_numbers(), name=session['name']), 200
    except:
        return "", 400

@app.route('/timeslots', methods=["GET","POST"]) 
def timeslot(): 
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        time_slot = request.form.get('timeslot')
        if len(session)==0:
            return redirect('/login')        
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).book(session['id'], time_slot)
            BCIT.save_to_json()
            email = Email()
            email.send_booking_confirmation(session['id'], room, time_slot)            
            return render_template('timeslot_rooms.html', rooms=BCIT.get_rooms_with_timeslot(time_slot), time_slot=time_slot, name=session['name']), 200
        if time_slot is not None and time_slot!="--Please choose a timeslot--":
            return render_template('timeslot_rooms.html', rooms=BCIT.get_rooms_with_timeslot(time_slot), time_slot=time_slot, name=session['name']), 200
        else:
            return render_template('timeslot.html', timeslots=BCIT.get_time_slots(), name=session['name']), 200
    except:
        return "", 400

@app.route('/view_bookings', methods=["GET","POST"]) 
def view_booking(): 
    if len(session)==0:
        return redirect('/login')
    id = session['id']
    path = './data/rooms.json'
    BCIT = Rooms(path)
    try:
        booking = request.form.get('booking')
        if len(session)==0:
            return redirect('/login')
        if request.method == 'POST' and booking is not None:
            room, time_slot = booking.split(',')
            BCIT.get_room(room).cancel_booking(id, time_slot)
            BCIT.save_to_json()
            email = Email()
            email.send_cancelling_confirmation(session['id'], room, time_slot)            
        return render_template('view_bookings.html', bookings=BCIT.get_booked_rooms(id), name=session['name']), 200    
    except:
        return "", 400

@app.route('/admin', methods=["GET","POST"])
def admin():
    if len(session)==0:
        return redirect('/login')
    try:
        return redirect("/admin/bookings")
    except:
        pass

@app.route('/admin/bookings', methods=["GET","POST"])
def admin_bookings():
    path = './data/rooms.json'
    BCIT = Rooms(path)
    users = Users()
    booking_details = []
    value = request.form.get('booking')
    if len(session)==0:
        return redirect('/login')
    if value is not None:
        room, id, time_slot = value.split(',')
        BCIT.get_room(room).cancel_booking(id, time_slot)
        BCIT.save_to_json()
        email = Email()
        email.send_cancelling_confirmation_admin(id, room, time_slot)  
    for booking in BCIT.get_all_booked_rooms():
        booking.append(users.get_name_from_id(booking[1]))
        booking_details.append(booking)
    try:
        if session['id']=='admin':
            return render_template('admin.html', bookings=booking_details, name=session['name']), 200
        else:
            return redirect('/login')
    except:
        pass

@app.route('/admin/approvals', methods=["GET","POST"])
def admin_approvals():
    if len(session)==0:
        return redirect('/login')
    users = Users()
    id = request.form.get('approval')
    if id is not None:
        users.approve_account(id)
        email = Email()
        # email.send_account_acceptance_confirmation(id)
    try:
        unapproved_users = users.get_unapproved_users()
        if session['id']=='admin':
            return render_template('admin_approve.html', name=session['name'], users=unapproved_users), 200
        else:
            return redirect('/login')
    except:
        pass

@app.route('/admin_clear_all', methods=["GET","POST"])
def admin_clear_all():
    if len(session)==0:
        return redirect('/login')
    path = './data/rooms.json'
    BCIT = Rooms(path)
    BCIT.clear_all_bookings()
    BCIT.save_to_json()
    try:
        if session['id']=='admin':
            return redirect('/admin')
        else:
            return redirect('/login')
    except:
        pass

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="0.0.0.0", port=port)