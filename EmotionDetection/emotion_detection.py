"""Emotion detection module powered by the embeddable Watson NLP library.

This module sends text to the Watson NLP EmotionPredict endpoint and returns
the scores for anger, disgust, fear, joy and sadness together with the
dominant emotion found in the text.
"""

import json
import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Detect the emotions expressed in the given text.

    Args:
        text_to_analyze (str): The text that has to be analysed.

    Returns:
        dict: The score of each emotion along with the dominant emotion. All
        the values are set to None when the server reports a blank entry
        (status code 400).
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    emotion_scores = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    return emotion_scores
