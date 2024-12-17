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
- Python 3.10
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



###6 Password Strength Checker

### Description 📄  
This project is a **Password Strength Checker** implemented in Python. It securely checks the strength of a user-provided password against predefined criteria and provides suggestions for improvement if the password is weak.

---

### Features 🚀  
1. **Secure Input**: Uses `getpass` to hide the password while typing.  
2. **Strength Validation**: Checks for:  
   - Minimum password length (8 characters)  
   - Presence of lowercase and uppercase letters  
   - Presence of at least one number  
   - Presence of at least one special character (`!@#$%^&*()`)  
3. **Interactive Feedback**: Provides clear, actionable suggestions to improve the password.  
4. **Loop Until Strong**: The program continues prompting until a strong password is entered.

---

### Technologies Used 🛠️  
- **Python 3**  
- **getpass**: For secure password input  
- **re (Regex)**: For pattern matching and validating password criteria  

---

### How to Run 💻  
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Run the Script**:  
   Run the Python file in your terminal or any Python IDE:  
   ```bash
   python password_strength_checker.py
   ```

3. **Input Password**:  
   Enter your password when prompted. The program will validate it and guide you to strengthen it if necessary.  

---

### Example Run 📋  
```bash
Enter your password: ********
Weak password. Improve it by fixing the following:
- Add at least one uppercase letter (A-Z).
- Add at least one special character (!, @, #, $, %, ^, &, *, (, )).

Enter your password: StrongPass123!
Password is strong! No one can hack your account.
```

---

### Password Strength Criteria ✅  
A strong password must satisfy the following conditions:  
1. **Minimum Length**: At least 8 characters.  
2. **Lowercase Letters**: Contains at least one lowercase letter (`a-z`).  
3. **Uppercase Letters**: Contains at least one uppercase letter (`A-Z`).  
4. **Numbers**: Contains at least one digit (`0-9`).  
5. **Special Characters**: Contains at least one symbol (`!@#$%^&*()`).  

---

### Contributing 🤝  
Contributions are welcome!  
1. Fork the repository.  
2. Create a new branch for your feature/bug fix:  
   ```bash
   git checkout -b my-new-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin my-new-feature
   ```
5. Open a Pull Request.  

---

### License 📝  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### Acknowledgments 🌟  
Special thanks to the Python community for their libraries and resources.  

---
