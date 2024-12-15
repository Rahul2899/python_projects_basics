# Python Projects Repository

This repository contains a collection of basic Python projects designed to enhance coding skills. Each project focuses on a specific concept or problem, providing practical hands-on experience with Python programming. Below is a description of each project and how to run them.

---

## Projects Included:

### 1. Calculator (`calculator.py`)
- **Description:** A simple calculator program that supports addition, subtraction, multiplication, and division.
- **Features:**
  - Menu-driven interface for selecting operations.
  - Handles invalid input and division by zero.
  - Allows repeated calculations until the user chooses to exit.
- **How to Run:**
  - Execute the script in a Python environment.
  - Follow the on-screen instructions to perform calculations.

---

### 2. Die Roll Simulator (`DieRoll.py`)
- **Description:** Simulates rolling a six-sided die and displays the outcome in a visual representation.
- **Features:**
  - Randomly generates numbers from 1 to 6.
  - Prints a simple graphical representation of the die face.
  - Allows the user to roll repeatedly until choosing to stop.
- **How to Run:**
  - Run the script and input `y` to roll the die or `n` to exit.
  - Handles invalid inputs gracefully.

---

### 3. Number Guessing Game (`NumberGuess.py`)
- **Description:** A fun guessing game where the user has five attempts to guess a randomly generated number between 0 and 100.
- **Features:**
  - Guides the user with hints (e.g., "Try smaller" or "Try larger").
  - Terminates early if the user guesses correctly.
  - Displays the correct answer if all attempts are used.
- **How to Run:**
  - Execute the script and follow the on-screen prompts.
  - Enter numbers within the specified range (0-100).

---

### 4. Screen Recorder (`practice.py`)
- **Description:** A screen recorder that captures the screen and saves the recording as a video file.
- **Features:**
  - Records the screen for a user-specified duration.
  - Displays a live preview while recording.
  - Outputs the recording as a `.avi` file.
- **How to Run:**
  - Install the required libraries: `opencv-python`, `pandas`, `numpy`, and `pyautogui`.
  - Run the script, enter the recording duration, and press `q` to stop early if needed.

---

### 5. Round Robin Scheduler (`RoundRobin.py`)
- **Description:** Implements a basic Round Robin scheduling algorithm for process management.
- **Features:**
  - Accepts user input for the number of processes, arrival times, and burst times.
  - Simulates Round Robin scheduling with a specified time quantum.
  - Displays waiting times and turn-around times for processes.
- **How to Run:**
  - Run the script and provide inputs as prompted.
  - Follow the output for scheduling details.

---

## Requirements:
- Python 3.x
- Required libraries:
  - `random`
  - `opencv-python`
  - `numpy`
  - `pandas`
  - `pyautogui`

---

## How to Use:
1. Clone the repository or download the files.
2. Install required libraries:
   ```bash
   pip install numpy pandas opencv-python pyautogui
