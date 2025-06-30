from flask import Flask, render_template, request, jsonify
from chat import get_response
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.moodify
journal_collection = db.journals
burnout_collection = db.burnout

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/journal', methods=['POST'])
def save_journal():
    data = request.get_json()
    journal_collection.insert_one({
        "entry": data['entry'],
        "timestamp": datetime.now().isoformat()
    })
    return jsonify({"message": "Journal saved!"})

@app.route('/get-journals')
def get_journals():
    entries = list(journal_collection.find({}, {"_id": 0}))
    return jsonify({"entries": entries})

if __name__ == "__main__":
    app.run(debug=True)
