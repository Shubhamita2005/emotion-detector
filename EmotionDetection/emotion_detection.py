import requests

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=json_data, headers=headers)

    # Handle error
    if response.status_code == 400:
        return None

    if response.status_code == 200:
        formatted_response = response.json()

        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "fear": emotions["fear"],
            "disgust": emotions["disgust"],
            "dominant_emotion": dominant_emotion
        }