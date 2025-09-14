import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    # URL of the Emotion Predict service of the Watson NLP Library.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the Emotion Predict service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the Emotion Predict API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting Emotion label and score from the response
    # If the response status code is 200, extract the emotions, score and dominant emotion from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    # If the response status code is 400, set all values to None
    elif response.status_code == 400:
        emotions = {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                    }

    # Returning a dictionary containing Emotion Set results
    return emotions
