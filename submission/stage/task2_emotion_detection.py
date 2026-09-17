"""Emotion detection application — Task 2 stage.

Copy this to the project root as `emotion_detection.py` to capture the Task 2
terminal output, where the function returns the raw response text.
"""

import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Send the text to the Watson NLP EmotionPredict function.

    Args:
        text_to_analyze (str): The text that has to be analysed.

    Returns:
        str: The text attribute of the response object.
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    return response.text
