"""Record the four terminal transcripts the AI grader asks for.

Run this in the Theia lab, from /home/project/final_project:

    python3 submission/capture.py

It drives a real python3 session for each question, so everything written to
submission/captured/ is genuine output from your own run.
"""

import os
import pty
import select
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "captured")


def record_session(lines, idle_limit=45.0):
    """Drive python3 inside a pty and return everything the terminal showed."""
    pid, fd = pty.fork()
    if pid == 0:
        os.chdir(ROOT)
        os.execvp("python3", ["python3"])

    captured = []
    pending = list(lines) + ["exit()"]
    last = time.time()
    time.sleep(0.6)

    while True:
        ready, _, _ = select.select([fd], [], [], 0.4)
        if ready:
            try:
                chunk = os.read(fd, 4096)
            except OSError:
                break
            if not chunk:
                break
            captured.append(chunk)
            last = time.time()
        elif pending:
            os.write(fd, (pending.pop(0) + "\n").encode())
            time.sleep(0.4)
            last = time.time()
        elif time.time() - last > idle_limit:
            break

    os.close(fd)
    os.waitpid(pid, 0)
    return b"".join(captured).decode("utf-8", "replace").replace("\r\n", "\n")


def write(name, header, body):
    """Save one transcript and echo it to the screen."""
    path = os.path.join(OUT, name)
    text = header + body.rstrip() + "\n"
    with open(path, "w") as handle:
        handle.write(text)
    print("\n" + "=" * 72)
    print(name)
    print("=" * 72)
    print(text)


def prompt_header():
    """Return a header showing the real working directory."""
    return "$ pwd\n%s\n$ python3\n" % os.getcwd()


def main():
    """Capture the transcripts for questions 3, 5, 7 and 9."""
    os.chdir(ROOT)
    os.makedirs(OUT, exist_ok=True)

    packaged = os.path.join(ROOT, "EmotionDetection", "emotion_detection.py")
    staged = os.path.join(HERE, "stage", "task2_emotion_detection.py")
    root_module = os.path.join(ROOT, "emotion_detection.py")

    print("Capturing Q3 (Task 2 stage, root-level import)...")
    shutil.copyfile(staged, root_module)
    write("q3_2b_application_creation.txt", prompt_header(), record_session([
        "from emotion_detection import emotion_detector",
        'emotion_detector("I love this new technology.")',
    ]))

    print("Capturing Q5 (formatted output, root-level import)...")
    shutil.copyfile(packaged, root_module)
    write("q5_3b_formatted_output_test.txt", prompt_header(), record_session([
        "from emotion_detection import emotion_detector",
        'emotion_detector("I am so happy I am doing this.")',
    ]))

    print("Capturing Q7 (packaged import path)...")
    write("q7_4b_packaging_test.txt", prompt_header(), record_session([
        "from EmotionDetection.emotion_detection import emotion_detector",
        'emotion_detector("I hate working long hours.")',
    ]))

    print("Capturing Q9 (unit tests)...")
    result = subprocess.run(
        [sys.executable, "test_emotion_detection.py"],
        cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False
    )
    write("q9_5b_unit_testing_result.txt",
          "$ pwd\n%s\n$ python3 test_emotion_detection.py\n" % ROOT,
          result.stdout.decode("utf-8", "replace"))

    os.remove(root_module)
    print("\nDone. Four transcripts are in submission/captured/.")
    print("Screenshots for Q11 and Q14 still have to be taken by hand:")
    print("  python3 server.py   ->  port 5000")


if __name__ == "__main__":
    main()
