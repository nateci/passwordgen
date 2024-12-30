import math
import re
from collections import Counter

class EntropyCalculator:
    @staticmethod
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
