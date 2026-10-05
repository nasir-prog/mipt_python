class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in pairs:
                if not stack or stack.pop() != pairs[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack
