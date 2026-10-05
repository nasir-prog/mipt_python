from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        for letter in ransomNote:
            if available[letter] == 0:
                return False
            available[letter] -= 1
        return True
