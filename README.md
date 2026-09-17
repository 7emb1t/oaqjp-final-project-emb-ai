# Final project

Repository for the final project of the *Developing AI Applications with Python
and Flask* course.

## Emotion Detection

An AI-based web application that runs analytics on customer feedback. The text
submitted by the customer is sent to the embeddable Watson NLP `EmotionPredict`
function, and the application reports the score of each emotion (anger,
disgust, fear, joy and sadness) together with the dominant emotion.

### Project structure

```text
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
└── test_emotion_detection.py
```

### Running the application

```bash
python3 server.py
```

The application is served on `localhost:5000`.

### Running the unit tests

```bash
python3 test_emotion_detection.py
```

> **Note:** the Watson NLP endpoint used by this project is hosted on the
> Skills Network platform and is only reachable from inside the Theia lab
> environment.
