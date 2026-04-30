from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle blank input
    if text_to_analyze is None or text_to_analyze == "":
        return "Invalid input! Please enter some text."

    response = emotion_detector(text_to_analyze)

    # Handle API error
    if response is None:
        return "Invalid input! Please enter some text."

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)