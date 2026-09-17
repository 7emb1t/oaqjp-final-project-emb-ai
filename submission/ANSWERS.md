# Final Project — Option 1 answer sheet (16 questions)

Repo: <https://github.com/7emb1t/oaqjp-final-project-emb-ai>

| Q | Task / Activity | Answer | Status |
|---|---|---|---|
| 1 | T1 — README URL | URL | ready |
| 2 | T2 A1 — `2a_emotion_detection` | code | ready |
| 3 | T2 A2 — `2b_application_creation` | terminal | needs lab |
| 4 | T3 A1 — `3a_output_formatting` | code | ready |
| 5 | T3 A2 — `3b_formatted_output_test` | terminal | needs lab |
| 6 | T4 A1 — `__init__.py` URL | URL | ready |
| 7 | T4 A2 — `4b_packaging_test` | terminal | needs lab |
| 8 | T5 A1 — `5a_unit_testing` | code | ready |
| 9 | T5 A2 — `5b_unit_testing_result` | terminal | needs lab |
| 10 | T6 A1 — `6a_server` | code | ready |
| 11 | T6 A2 — `6b_deployment_test.png` | upload | needs lab |
| 12 | T7 A1 — `7a_error_handling_function` | code | ready |
| 13 | T7 A2 — `7b_error_handling_server` | code | ready |
| 14 | T7 A3 — `7c_error_handling_interface.png` | upload | needs lab |
| 15 | T8 A1 — `8a_server_modified` | code | ready |
| 16 | T8 A2 — `8b_static_code_analysis` | terminal | ready (10.00/10) |

---

## Question 1 — URL

```
https://github.com/7emb1t/oaqjp-final-project-emb-ai/blob/main/README.md
```

---

## Question 2 — Task 2, Activity 1

Paste this (the `emotion_detection.py` application function):

```python
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
```

---

## Question 3 — Task 2, Activity 2

**Needs the Theia lab** — the Watson endpoint is unreachable outside it. In the lab, inside `final_project`:

```
python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
```

Paste the whole block — the three steps plus the returned dictionary. That shows
the application imported and tested without errors, which is what the question asks for.

---

## Question 4 — Task 3, Activity 1

Paste the same `emotion_detection.py` as Question 2 — it is the version whose
`emotion_detector` returns the required output format:

```python
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
```

---

## Question 5 — Task 3, Activity 2

**Needs the Theia lab** — the Watson endpoint is unreachable outside it.

```
python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this.")
```

Confirm `'dominant_emotion': 'joy'`, then paste the block.

---

## Question 6 — URL

```
https://github.com/7emb1t/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

For reference, that file contains:

```python
"""EmotionDetection package.

Exposes the emotion_detector function of the emotion_detection module so the
application can be imported as `from EmotionDetection import emotion_detector`.
"""

from . import emotion_detection
from .emotion_detection import emotion_detector
```

---

## Question 7 — Task 4, Activity 2

**Needs the Theia lab** — the Watson endpoint is unreachable outside it.

```
python3
>>> from EmotionDetection import emotion_detector
>>> emotion_detector("I hate working long hours.")
```

Confirm `'dominant_emotion': 'anger'`, then paste the block.

---

## Question 8 — Task 5, Activity 1

```python
"""Unit tests for the emotion_detector function of the EmotionDetection package."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test that emotion_detector returns the expected dominant emotion."""

    def test_joy(self):
        """The statement should be detected as joy."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """The statement should be detected as anger."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """The statement should be detected as disgust."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """The statement should be detected as sadness."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """The statement should be detected as fear."""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
```

---

## Question 9 — Task 5, Activity 2

**Needs the Theia lab** — the Watson endpoint is unreachable outside it.

```
python3 test_emotion_detection.py
```

Paste the result — expect `Ran 5 tests in <n>s` followed by `OK`.

---

## Question 10 — Task 6, Activity 1

```python
"""Flask server that deploys the emotion detection application on the web.

The application exposes the `/emotionDetector` route, which analyses the text
submitted by the user and returns a formatted sentence describing the emotions
found in it.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Analyse the text sent by the user and return the formatted response.

    Returns:
        str: A sentence listing every emotion score and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the landing page of the application.

    Returns:
        str: The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Question 11 — Upload `6b_deployment_test.png`

**Needs the Theia lab** — the Watson endpoint is unreachable outside it. Run `python3 server.py`, open the app on port 5000, enter
**`I think I am having fun`**, click *Run Sentiment Analysis*, and screenshot the
page showing the system response with `The dominant emotion is joy.`

---

## Question 12 — Task 7, Activity 1

```python
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
```

The `status_code == 400` branch is the part this question is graded on.

---

## Question 13 — Task 7, Activity 2

```python
"""Flask server that deploys the emotion detection application on the web.

The application exposes the `/emotionDetector` route, which analyses the text
submitted by the user and returns a formatted sentence describing the emotions
found in it.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Analyse the text sent by the user and return the formatted response.

    Returns:
        str: A sentence listing every emotion score and the dominant emotion,
        or an error message when the submitted text is blank.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the landing page of the application.

    Returns:
        str: The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

The `if dominant_emotion is None:` branch returning `Invalid text! Please try again!`
is the part this question is graded on.

---

## Question 14 — Upload `7c_error_handling_interface.png`

**Needs the Theia lab** — the Watson endpoint is unreachable outside it. With the server running, leave the input box blank, click
*Run Sentiment Analysis*, and screenshot the page showing
**`Invalid text! Please try again!`**

---

## Question 15 — Task 8, Activity 1

Same `server.py` as Question 13 — it is the file that scores 10/10:

```python
"""Flask server that deploys the emotion detection application on the web.

The application exposes the `/emotionDetector` route, which analyses the text
submitted by the user and returns a formatted sentence describing the emotions
found in it.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Analyse the text sent by the user and return the formatted response.

    Returns:
        str: A sentence listing every emotion score and the dominant emotion,
        or an error message when the submitted text is blank.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the landing page of the application.

    Returns:
        str: The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Question 16 — Task 8, Activity 2

```
$ pylint server.py


------------------------------------
Your code has been rated at 10.00/10
```

Verified locally on this exact `server.py`. Re-run `pylint server.py` in the lab
and paste that transcript if you want the lab's own output.

---

## Note on Questions 2, 4 and 12

They all take the same `emotion_detection.py`, because the final file is a
superset: it defines the application function (Q2), returns the required
dictionary format (Q4), and handles status code 400 (Q12). Submitting the final
file for all three cannot be marked down for a missing feature.

If you would rather submit the literal Task 2 stage for Q2 — the version that
returns `response.text` before Task 3 modifies it — it is saved at
`submission/2a_emotion_detection.txt`. If you use it, capture Q3's output from
that same version so the two answers agree.
