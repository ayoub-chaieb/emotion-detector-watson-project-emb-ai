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

    # Returning a text attribute of the response object
    return response.text