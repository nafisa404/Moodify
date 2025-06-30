# 🎧 Moodify - Mood-Based Music Recommender

Moodify is an AI-powered web application that curates music recommendations based on your current mood. By analyzing facial expressions, text input, or user selections, Moodify connects you with the perfect playlist — anytime, anywhere.

![Moodify Banner](assets/banner.png) <!-- Optional: Add a project banner image -->

---

## 🌟 Features

- 🎭 **Mood Detection**: Detects user mood via facial recognition or text sentiment.
- 🎵 **Spotify Integration**: Automatically plays music based on detected mood.
- 📈 **Mood History Tracker**: Keeps track of mood trends over time.
- 🔒 **User Authentication**: Sign in to save preferences and mood logs.
- 📱 **Responsive UI**: Works seamlessly on mobile, tablet, and desktop.

---

## 🛠️ Tech Stack

| Frontend         | Backend           | AI/ML             | Others            |
|------------------|-------------------|-------------------|-------------------|
| React.js         | Node.js / Flask   | TensorFlow / OpenCV | Spotify Web API  |
| Tailwind CSS     | Express / Flask   | NLP (TextBlob/VADER) | JWT Auth         |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nafisa404/Moodify.git
cd Moodify
```

### 2. Install dependencies

#### Frontend

```bash
cd client
npm install
npm start
```

#### Backend

```bash
cd server
pip install -r requirements.txt
python app.py
```

> Ensure you have `.env` files set up for both frontend and backend (see `.env.example`).

---

## 🧪 Example Moods & Music

| Mood      | Playlist/Genre     |
|-----------|--------------------|
| Happy     | Pop, Dance Hits    |
| Sad       | Acoustic, Blues    |
| Angry     | Rock, Metal        |
| Calm      | Lo-Fi, Instrumental|

---

## 📁 Project Structure

```
Moodify/
├── client/                 # React frontend
│   ├── public/
│   └── src/
├── server/                 # Flask/Node backend
│   └── app.py
├── models/                 # ML models and scripts
├── assets/                 # Images, logos, etc.
├── README.md
└── .env.example
```

---

## ✅ TODOs / Improvements

- [ ] Add journaling feature with AI mood summary
- [ ] Enable social sharing of mood-based playlists
- [ ] Integrate more music APIs (YouTube, Apple Music)
- [ ] Add dark/light mode toggle

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you’d like to change. Then:

```bash
git checkout -b feature/my-new-feature
git commit -m "Add new feature"
git push origin feature/my-new-feature
```

---


## 🙋‍♀️ About the Creator

Built with ❤️ by [Nafisa Tahasin](https://github.com/nafisa404) — passionate about using AI to create meaningful digital experiences.
