# Emotion-Based Music Recommender System

## Project Overview
This project is an innovative blend of Natural Language Processing (NLP) and API integration, designed to analyze the emotion conveyed in a user's text input and recommend music tracks that align with the detected emotion. Utilizing Hugging Face's Transformers for emotion detection and the Spotify API for fetching music recommendations, this application offers a unique way to explore the connection between music and emotions.

## Features
- **Emotion Detection**: Analyze text input to detect underlying emotions.
- **Music Recommendation**: Spotify API to recommend music tracks based on the detected emotion.
- **Interactive Web Interface**: A Flask-based web application that allows users to enter text and receive personalized music recommendations.

## Technology Stack
- **Python**: The primary programming language used.
- **Flask**: A micro web framework for serving the web application.
- **Transformers and Datasets Libraries**: From Hugging Face for leveraging pre-trained NLP models.
- **Spotipy**: A lightweight Python library for the Spotify Web API.
- **PyTorch**: Utilized for model training and inference.

## How to Use
Navigate to the `src` directory and run the Flask application:

```python
cd src
python app.py
```
After starting the application, open your web browser and navigate to `http://localhost:5000` to access the interactive interface.

## Model Training
The emotion detection model is trained on the "emotion" dataset from Hugging Face's datasets library, utilizing a DistilBERT model fine-tuned for emotion classification. The model distinguishes between six emotions: sadness, joy, love, anger, fear, and surprise, offering a nuanced understanding of text input.

## Spotify API Integration
Music recommendations are fetched using the Spotify API, which queries for playlists matching the detected emotion. The application then selects tracks from these playlists to recommend to the user, creating a personalized music experience based on their emotional state.

## Project Structure
```python
EmotionBasedMusicRecommender/
│
├── notebooks/                   # Jupyter notebooks for model training
│   └── EmotionMusicRec.ipynb
├── emotion_detection_model/     # Trained model and tokenizer
├── src/                         # Flask application source code
│   ├── static/                  # CSS for the web app
│   ├── templates/               # HTML templates
│   ├── app.py                   # Flask application entry point
│   └── spotify_integration.py   # Spotify API integration
├── .env                         # Environment variables (API keys)
├── .gitignore                   # Files to ignore in version control
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Acknowledgements
Special thanks to Hugging Face for providing the Transformers and Datasets libraries, the creators of the Spotipy library, and Spotify for their comprehensive API."# Emotion-Based-Music_Recommender" 
"# Emotion-Based-Music_Recommender" 
