import requests

def emotion_detector(text_to_analyze):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_ID/v1/analyze"

    headers = {"Content-Type": "application/json"}

    json_data = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }

    response = requests.post(url, json=json_data, headers=headers)

    if response.status_code == 400:
        return None

    if response.status_code == 200:
        emotions = response.json()["emotion"]["document"]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "fear": emotions["fear"],
            "disgust": emotions["disgust"],
            "dominant_emotion": dominant_emotion
        }