class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""

        for i in s:
            if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
                clean = clean + i

        s1 = list(clean)
        s2 = ""
        while len(s1) != 0:
            s2 = s2 + s1.pop()
        
        return s2 == clean
        