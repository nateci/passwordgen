import re
from collections import Counter

class PasswordAnalyzer:
    @staticmethod
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

