class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        previous = 0
        for symbol in reversed(s):
            value = values[symbol]
            if value < previous:
                total -= value
            else:
                total += value
            previous = value
        return total
