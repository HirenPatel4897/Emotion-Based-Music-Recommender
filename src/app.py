from flask import Flask, render_template, request
from spotify_integration import get_spotify_recommendations
from emotion_predictor import predict_emotion
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text_input']
        emotion = predict_emotion(text)
        recommendations = get_spotify_recommendations(emotion)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
