import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.moodify
burnout_collection = db.burnout

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = 'data.pth'
data = torch.load(FILE)

model = NeuralNet(data["input_size"], data["hidden_size"], data["output_size"]).to(device)
model.load_state_dict(data["model_state"])
model.eval()

all_words = data['all_words']
tags = data['tags']

def log_mood(mood):
    burnout_collection.insert_one({
        "mood": mood,
        "timestamp": datetime.now().isoformat()
    })

def detect_burnout():
    week_ago = datetime.now() - timedelta(days=7)
    logs = list(burnout_collection.find({"timestamp": {"$gte": week_ago.isoformat()}}))
    negative_moods = [log for log in logs if log['mood'] in ["sad", "angry", "anxious"]]
    if len(negative_moods) > 4:
        return "I’ve noticed some consistent low moods. Would you like to talk about it or try a calming activity?"
    return None

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = torch.from_numpy(X).float().to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    if probs[0][predicted.item()] > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                log_mood(tag)
                burnout_msg = detect_burnout()
                if burnout_msg:
                    return burnout_msg
                return random.choice(intent['responses'])
    return "I'm not sure I understand. Could you rephrase?"
