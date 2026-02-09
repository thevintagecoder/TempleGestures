# AI Temple Run Controller

A Computer Vision project I made that allows you to play _Temple Run_ using only hand gestures. Built with Python, OpenCV, and MediaPipe.

## Tech Stack

- **Language:** Python 3.11
- **Vision:** OpenCV & Google MediaPipe
- **Automation:** PyAutoGUI

## Features

- **Jump:** Open your hand (5 fingers).
- **Slide:** Make a fist (0 fingers).
- **Turn Left/Right:** Move your hand to the screen edges.
- **Smooth Control:** Uses a stability buffer to prevent jittery inputs.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/TempleRun-CV-Controller.git](https://github.com/YOUR_USERNAME/TempleRun-CV-Controller.git)
    cd TempleRun-CV-Controller
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the controller:
    ```bash
    python main.py
    ```
4.  Open [Temple Run Web](https://poki.com/en/g/temple-run-2) and start playing!

## How it Works

1.  **Detection:** Uses MediaPipe to track 21 hand landmarks in real-time.
2.  **Logic:** Calculates finger states (folded vs. open) and wrist position (X-coordinates).
3.  **Action:** Maps these states to keyboard inputs (`Arrow Keys`) using PyAutoGUI.
