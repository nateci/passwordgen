# 🔐 Password Strength Visualizer & Generator

This project evaluates **password strength**, analyzes weaknesses, and generates **stronger password suggestions**. It uses entropy calculations to measure security and provides **real-time feedback** through a user-friendly GUI.

---

## 📌 Features
- **Entropy Calculation**: Measures password strength in bits.
- **Weakness Detection**: Identifies common vulnerabilities (e.g., weak patterns, repetition).
- **Password Suggestions**: Generates 8 stronger alternatives.
- **GUI-Based Evaluation**: Simple `tkinter` interface for user input.

---

## 🏗️ Project Structure
```
passwordgen/
├── entropy_calculator.py  # Calculates password entropy
├── password_analyzer.py   # Identifies password weaknesses
├── password_generator.py  # Generates secure password suggestions
├── gui.py                 # GUI for evaluating passwords
├── main.py                # Entry point for running the app
├── requirements.txt       # Dependencies list
└── README.md              # Project documentation
```

---

## ⚙️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/passwordgen.git
cd passwordgen
```

### 2️⃣ Install Dependencies
Make sure you have Python 3 installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```
Alternatively, install them manually:
```bash
pip install tkinter
```

### 3️⃣ Run the Application
```bash
python main.py
```

---

## 📂 Code Overview

### 🔢 `entropy_calculator.py` (Entropy Calculation)
```python
import math
import re

class EntropyCalculator:
    @staticmethod
    def calculate_entropy(password):
        length = len(password)
        charset_size = 0

        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32

        if charset_size == 0:
            return 0

        return length * math.log2(charset_size)
```
- Determines **character set size** (lowercase, uppercase, digits, special characters).
- Computes **password entropy** using `H = L * log2(C)`.

---

### 🕵️ `password_analyzer.py` (Weakness Analysis)
```python
import re
from collections import Counter

class PasswordAnalyzer:
    @staticmethod
    def analyze_weaknesses(password):
        weaknesses = []

        if len(password) < 8:
            weaknesses.append("Too short (less than 8 characters)")

        if re.search(r'(1234|password|qwerty|abcd|letmein)', password.lower()):
            weaknesses.append("Contains common patterns or words")

        counts = Counter(password)
        if any(count > len(password) / 2 for count in counts.values()):
            weaknesses.append("Too many repeated characters")

        if not re.search(r'[a-z]', password):
            weaknesses.append("No lowercase letters")
        if not re.search(r'[A-Z]', password):
            weaknesses.append("No uppercase letters")
        if not re.search(r'[0-9]', password):
            weaknesses.append("No digits")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            weaknesses.append("No special characters")

        return weaknesses
```
- Checks for **common passwords**, **short length**, **repeated characters**, and **lack of variety**.

---

### 🛠️ `password_generator.py` (Password Suggestions)
```python
import random
import string

class PasswordGenerator:
    @staticmethod
    def generate_suggestions(password):
        suggestions = []
        base_chars = string.ascii_letters + string.digits + string.punctuation

        for _ in range(8):
            suggestion = list(password)

            while len(suggestion) < 8:
                suggestion.insert(random.randint(0, len(suggestion)), random.choice(base_chars))

            if not any(c.isupper() for c in suggestion):
                suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.ascii_uppercase))
            if not any(c.isdigit() for c in suggestion):
                suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.digits))
            if not any(c in string.punctuation for c in suggestion):
                suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.punctuation))

            suggestions.append(''.join(suggestion))

        return suggestions
```
- Generates **stronger variations** of the input password.
- Ensures passwords include **upper/lowercase letters, digits, and symbols**.

---

### 🖥️ `gui.py` (Graphical User Interface)
Provides an **interactive tkinter-based** interface.
```python
import tkinter as tk
from tkinter import messagebox
from entropy_calculator import EntropyCalculator
from password_analyzer import PasswordAnalyzer
from password_generator import PasswordGenerator

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Visualizer")
        self.root.geometry("600x400")

        label = tk.Label(root, text="Enter a password to evaluate:")
        label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        button = tk.Button(root, text="Evaluate Password", command=self.evaluate_password_gui)
        button.pack(pady=20)

    def evaluate_password_gui(self):
        password = self.entry.get()
        entropy = EntropyCalculator.calculate_entropy(password)
        weaknesses = PasswordAnalyzer.analyze_weaknesses(password)

        suggestions = PasswordGenerator.generate_suggestions(password)
        suggestion_entropies = [EntropyCalculator.calculate_entropy(s) for s in suggestions]

        analysis_text = f"Entropy: {entropy:.2f} bits\n\nWeaknesses:\n"
        for weakness in weaknesses:
            analysis_text += f"- {weakness}\n"

        analysis_text += "\nSuggestions:\n"
        for i, (s, e) in enumerate(zip(suggestions, suggestion_entropies)):
            analysis_text += f"{i+1}. {s} (Entropy: {e:.2f} bits)\n"

        messagebox.showinfo("Password Analysis", analysis_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
```
- Users **input a password** and get **entropy, weaknesses, and suggestions**.

---

## 💡 Future Enhancements
✅ Implement **machine learning-based password strength scoring**  
✅ Add **real-time keystroke-based password evaluation**  
✅ Introduce **integration with password managers**  

---

## 🏆 Contributors
- **John Atkins**  
- Open-source contributions are welcome! Submit a **pull request**.  

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

### ⭐ Show Some Support!
If you found this useful, please **star** 🌟 this repository and **fork** 🍴 it to contribute!  
