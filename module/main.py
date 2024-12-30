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

        # Generate 8 password suggestions
        suggestions = PasswordGenerator.generate_suggestions(password)
        suggestion_entropies = [EntropyCalculator.calculate_entropy(s) for s in suggestions]

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

        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("Password Analysis")
        tk.Label(analysis_window, text=analysis_text, justify="left").pack(pady=10)

        for i in range(8):
            tk.Button(analysis_window, text=f"Select {i+1}", command=lambda i=i: select_suggestion(i)).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
