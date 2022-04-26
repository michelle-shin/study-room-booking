from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/') 
def homepage(): 
    try:
        return render_template('home.html'), 200
    except:
        return "", 400

if __name__ == "__main__":
    app.run()