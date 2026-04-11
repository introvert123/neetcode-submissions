class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(',']':'[','}':'{'}
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif stack and dict1[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0

        