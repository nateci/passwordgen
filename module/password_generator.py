import random
import string

class PasswordGenerator:
    @staticmethod
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
