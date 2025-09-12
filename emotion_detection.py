# Import the Flask class from the flask module
from flask import Flask
import json

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)


url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
input_json={ "raw_document": { "text": text_to_analyse } }
text_to_analyse=""

def emotion_detector(text_to_analyse):
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)