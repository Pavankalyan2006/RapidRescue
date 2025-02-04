from flask import Flask, redirect, render_template, request, session, url_for, flash, jsonify
from twilio.rest import Client
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure, random key

# Twilio credentials
account_sid = "Enter your key"
auth_token = "Enter your Token"
twilio_phone_number = "Enter your number"

# Dummy in-memory storage for registered users
users = {}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid login details, please try again.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            session['username'] = username  # Log in automatically after registration
            return redirect(url_for('home'))
        flash('Username already exists.')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/ambulance_service', methods=['GET', 'POST'])
def ambulance_service():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        phone_number = request.form['phone_number']
        message = request.form['message']

        client = Client(account_sid, auth_token)
        try:
            client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=phone_number
            )
            flash("Message sent successfully!")
        except Exception as e:
            flash(f"Failed to send message: {e}")

    return render_template('ambulance_service.html')

@app.route('/hospitals')
def hospitals():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('hospitals.html')

@app.route('/medications')
def medications():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('medications.html')

@app.route('/get_medications', methods=['GET'])
def get_medications():
    disease = request.args.get('disease')
    medications = []

    if disease:
        url = f"https://api.fda.gov/drug/label.json?search=indications_and_usage:{disease}&limit=100"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            medications = [{
                "brand_name": med.get('openfda', {}).get('brand_name', ['N/A'])[0],
                "generic_name": med.get('openfda', {}).get('generic_name', ['N/A'])[0],
                "indications": med.get('indications_and_usage', ['N/A'])[0]
            } for med in results]

    return jsonify(medications)
@app.route('/calculate_distance', methods=['GET'])
def calculate_distance():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    api_key = '5b3ce3597851110001cf6248bec150618dda48c18599decf14c6b8e4'
    
    url = f"https://api.openrouteservice.org/v2/matrix/driving-car?api_key={api_key}"
    body = {
        "locations": [
            [float(origin.split(',')[1]), float(origin.split(',')[0])],  # [lng, lat]
            [float(destination.split(',')[1]), float(destination.split(',')[0])]
        ],
        "metrics": ["distance"]
    }

    response = requests.post(url, json=body)

    if response.status_code == 200:
        distances = response.json()
        distance = distances['distances'][0][1]  # Distance between the first two locations
        return jsonify({"distance": distance})
    else:
        return jsonify({"error": "Unable to calculate distance"}), 500
if __name__ == "__main__":
    app.run(debug=True)
