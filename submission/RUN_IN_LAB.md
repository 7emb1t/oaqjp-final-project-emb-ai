# Run in the Theia lab — capture the remaining deliverables

The Watson NLP endpoint (`sn-watson-emotion.labs.skills.network`) resolves to a
private Skills Network address (`10.241.64.14`) and is **only reachable from
inside the Theia lab**, exactly as the project PDF warns. All the code is
written, linted and logic-verified; these steps only capture the live outputs.

## 0. Get the code into the lab

Open a terminal in the Theia lab and run:

```bash
git clone https://github.com/7emb1t/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install requests flask pylint
```

## 1. Task 2 — Activity 2 → `2b_application_creation`

```bash
python3
```
```python
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I love this new technology.")
```
Copy the whole terminal block (the three steps + output) into
`2b_application_creation.txt`.

> Note: the repo already contains the **final** version of the function, which
> returns the formatted dictionary rather than the raw response text. That is
> fine for grading — the Task 2 raw-text version is preserved in
> `2a_emotion_detection.txt`. If you want the literal Task 2 output, temporarily
> `return response.text`, capture it, then restore.

## 2. Task 3 — Activity 2 → `3b_formatted_output_test`

```python
emotion_detector("I am so happy I am doing this.")
```
Confirm `'dominant_emotion': 'joy'`. Paste into `3b_formatted_output_test.txt`.

## 3. Task 4 — Activity 2 → `4b_packaging_test`

```bash
python3
```
```python
from EmotionDetection import emotion_detector
emotion_detector("I hate working long hours.")
```
Confirm `'dominant_emotion': 'anger'`. Paste into `4b_packaging_test.txt`.

## 4. Task 5 — Activity 2 → `5b_unit_testing_result`

```bash
python3 test_emotion_detection.py
```
Expect `Ran 5 tests ... OK`. Paste into `5b_unit_testing_result.txt`.

## 5. Task 6 — Activity 2 → `6b_deployment_test.png`

```bash
python3 server.py
```
Open the app on port **5000** (Skills Network → *Launch Application* → port 5000).
Enter **`I think I am having fun`**, click *Run Sentiment Analysis*, and
screenshot the page showing:

> For the given statement, the system response is 'anger': …, 'disgust': …,
> 'fear': …, 'joy': … and 'sadness': …. The dominant emotion is joy.

Save as `6b_deployment_test.png`.

## 6. Task 7 — Activity 3 → `7c_error_handling_interface.png`

With the server still running, leave the input box **blank** and click
*Run Sentiment Analysis*. Screenshot the page showing:

> Invalid text! Please try again!

Save as `7c_error_handling_interface.png`.

## 7. Task 8 — Activity 2 → `8b_static_code_analysis`

```bash
pylint server.py
```
Expect `Your code has been rated at 10.00/10`. (Already verified locally — see
`8b_static_code_analysis.txt`; re-run in the lab and paste the lab transcript.)

## 8. Push any edits back

```bash
git add . && git commit -m "Final project deliverables" && git push
```
