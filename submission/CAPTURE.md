# Capturing the six failed answers (Q3, Q5, Q7, Q9, Q11, Q14)

All six are **live evidence** — real terminal transcripts and real screenshots.
They cannot be written in advance, and the four text ones scored 0/1 because the
command alone was submitted without the output it produces.

Two rubric details the grader's feedback revealed:

1. **Q3 and Q5 want the root-level import** `from emotion_detection import emotion_detector`
   — not the packaged path. Task 2 and Task 3 happen *before* packaging, so
   `emotion_detection.py` must sit in the project root at that point.
2. **Q7 wants the full packaged path** `from EmotionDetection.emotion_detection import emotion_detector`
   — not the `from EmotionDetection import emotion_detector` shortcut.
3. **Q3 also wants the prompt line visible**, showing `/home/project/final_project`.
   So copy the transcript starting at the `$` prompt, not at the word `python3`.

## Setup — clone to the exact expected path

In the Theia lab terminal:

```bash
cd /home/project
git clone https://github.com/7emb1t/oaqjp-final-project-emb-ai.git final_project
cd /home/project/final_project
python3 -m pip install requests flask pylint
```

Confirm the prompt reads `/home/project/final_project` before continuing.

## Q3 — Task 2, Activity 2

Put the Task 2 version of the module at the project root, then run it:

```bash
cp submission/stage/task2_emotion_detection.py emotion_detection.py
python3
```
```python
from emotion_detection import emotion_detector
emotion_detector("I love this new technology.")
```
Then `exit()`.

Select and copy **everything from the `$` prompt line down to and including the
long JSON string** that comes back. That JSON is the "long dictionary-structured
output" the rubric asks for. Paste that whole block into Q3.

## Q5 — Task 3, Activity 2

Now swap in the formatted version and run again:

```bash
cp EmotionDetection/emotion_detection.py emotion_detection.py
python3
```
```python
from emotion_detection import emotion_detector
emotion_detector("I am so happy I am doing this.")
```

Copy the prompt line, both statements, and the returned dictionary. It must show
all five scores plus `'dominant_emotion': 'joy'`. Paste into Q5.

## Q7 — Task 4, Activity 2

Use the **full packaged import path** here:

```bash
python3
```
```python
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I hate working long hours.")
```

Copy the prompt line, both statements, and the dictionary showing
`'dominant_emotion': 'anger'`. Paste into Q7.

## Q9 — Task 5, Activity 2

```bash
python3 test_emotion_detection.py
```

Copy the command **and** everything it prints — the dots or test names, the
`Ran 5 tests in <n>s` line, and the final `OK`. Paste into Q9.

## Q11 — Task 6, Activity 2 (upload)

```bash
python3 server.py
```

Skills Network → *Launch Application* → port **5000**. Type
`I think I am having fun`, click *Run Sentiment Analysis*, wait for the response
line to appear, then screenshot the page. It must show the scores and
`The dominant emotion is joy.`

Save as `6b_deployment_test.png` and upload it. This question was submitted
blank, which is why it scored 0.

## Q14 — Task 7, Activity 3 (upload)

Same running server. Clear the input box completely, click
*Run Sentiment Analysis*, and screenshot the page showing
`Invalid text! Please try again!`

Save as `7c_error_handling_interface.png` and upload it.

## Tidy up afterwards

The root-level `emotion_detection.py` was only needed for the Q3 and Q5
captures. The packaged copy under `EmotionDetection/` is the real one:

```bash
rm emotion_detection.py
git add . && git commit -m "Final project" && git push
```
