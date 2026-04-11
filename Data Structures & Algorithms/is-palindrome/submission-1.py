class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        left = 0
        right = n - 1

        s = s.lower()
        while left <= right:
            if self.isValidChar(s[left]) and self.isValidChar(s[right]):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not self.isValidChar(s[left]):
                    left += 1
                if not self.isValidChar(s[right]):
                    right -= 1 

        return True
    
    def isValidChar(self, c: char) -> bool:
        if c >= 'a' and c <= 'z' or c >= '0' and c <= '9':
            return True
        else:
            return False