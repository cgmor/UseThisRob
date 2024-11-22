from flask import Blueprint, jsonify, request
from app.database import fetch_table_data
from app.twilio_handler import send_text
from app.proximity_helper import check_proximity_and_notify
from app.analyzer import analyze_text

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask server!"

@main.route('/send-text')
def send():
    send_text()
    return jsonify({"status": "Text sent successfully"}), 200

@main.route('/analyze-text', methods=['POST'])
def analyze():
    text = request.json.get('transcript')
    analysis = analyze_text(text)
    print(analysis)
    return jsonify(analysis)

@main.route('/customer-data', methods=['GET'])
def customer_data():
    data = fetch_table_data()
    print(data)
    return jsonify(data)

@main.route('/check-proximity', methods=['POST'])
def check_proximity():
    data = request.json
    print(f"Raw data is {data}")
    target_address = data.get("address")
    print(f"Target addy is {target_address}")
    
    if not target_address:
        return jsonify({"error": "No address provided"}), 400
    
    # Call the function
    check_proximity_and_notify(target_address)
    return jsonify({"message": "Proximity check complete"})