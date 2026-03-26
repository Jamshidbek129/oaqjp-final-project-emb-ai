from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is {response}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return "Welcome to Emotion Detector"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
