from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get("textToAnalyze")

    if not text:
        return "Invalid input! Please enter some text."

    result = emotion_detector(text)

    if result is None:
        return "Invalid input! Please enter some text."

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)