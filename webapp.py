from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"]) 
def homepage(): 
    try:
        if request.method == 'POST':
            room_number = request.form.get('room')
            return render_template('room.html', room=room_number), 200
        else:
            return render_template('home.html'), 200
    except:
        return "", 400

if __name__ == "__main__":
    app.run(debug=True)