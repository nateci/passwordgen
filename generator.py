import math
import re
from collections import Counter
import random
import string
import tkinter as tk
from tkinter import messagebox

# Entropy Calculation
def calculate_entropy(password):
    length = len(password)
    charset_size = 0

    # Determine character set size
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

    entropy = length * math.log2(charset_size)
    return entropy

# Check for Weaknesses
def analyze_weaknesses(password):
    weaknesses = []

    # Length Check
    if len(password) < 8:
        weaknesses.append("Too short (less than 8 characters)")

    # Common Patterns
    if re.search(r'(1234|password|qwerty|abcd|letmein)', password.lower()):
        weaknesses.append("Contains common patterns or words")

    # Repeated Characters
    counts = Counter(password)
    if any(count > len(password) / 2 for count in counts.values()):
        weaknesses.append("Too many repeated characters")

    # Lack of Character Variety
    if not re.search(r'[a-z]', password):
        weaknesses.append("No lowercase letters")
    if not re.search(r'[A-Z]', password):
        weaknesses.append("No uppercase letters")
    if not re.search(r'[0-9]', password):
        weaknesses.append("No digits")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        weaknesses.append("No special characters")

    return weaknesses

# Generate Password Suggestions based on improvements
def generate_suggestions(password):
    suggestions = []
    base_chars = string.ascii_letters + string.digits + string.punctuation

    # Generate 8 variations with different patterns to address weaknesses
    for _ in range(8):
        suggestion = list(password)

        # Ensure length is at least 8
        while len(suggestion) < 8:
            suggestion.insert(random.randint(0, len(suggestion)), random.choice(base_chars))

        # Ensure character variety
        if not any(c.isupper() for c in suggestion):
            suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.ascii_uppercase))
        if not any(c.isdigit() for c in suggestion):
            suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.digits))
        if not any(c in string.punctuation for c in suggestion):
            suggestion.insert(random.randint(0, len(suggestion)), random.choice(string.punctuation))

        suggestions.append(''.join(suggestion))

    return suggestions

# GUI Function
def evaluate_password_gui():
    password = entry.get()
    entropy = calculate_entropy(password)
    weaknesses = analyze_weaknesses(password)

    # Generate 8 password suggestions
    suggestions = generate_suggestions(password)
    suggestion_entropies = [calculate_entropy(s) for s in suggestions]

    # Display weaknesses, entropy, and suggestions
    analysis_text = f"Entropy: {entropy:.2f} bits\n\nWeaknesses:\n"
    if weaknesses:
        for weakness in weaknesses:
            analysis_text += f"- {weakness}\n"
    else:
        analysis_text += "No weaknesses found\n"

    analysis_text += "\nSuggestions:\n"
    for i, (s, e) in enumerate(zip(suggestions, suggestion_entropies)):
        analysis_text += f"{i+1}. {s} (Entropy: {e:.2f} bits)\n"

    # Show analysis in a new window
    def select_suggestion(index):
        selected_password = suggestions[index]
        selected_entropy = suggestion_entropies[index]
        messagebox.showinfo("Selection", f"You've chosen: {selected_password}\nEntropy: {selected_entropy:.2f} bits")

    analysis_window = tk.Toplevel(root)
    analysis_window.title("Password Analysis")
    tk.Label(analysis_window, text=analysis_text, justify="left").pack(pady=10)

    for i in range(8):
        tk.Button(analysis_window, text=f"Select {i+1}", command=lambda i=i: select_suggestion(i)).pack(pady=5)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Visualizer")
root.geometry("600x400")

label = tk.Label(root, text="Enter a password to evaluate:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button = tk.Button(root, text="Evaluate Password", command=evaluate_password_gui)
button.pack(pady=20)

root.mainloop()
