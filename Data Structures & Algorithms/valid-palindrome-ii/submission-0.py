class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                skipLeft = s[left+1:right+1]
                skipRight = s[left:right]

                if (skipLeft[::-1] == skipLeft) or (skipRight[::-1] == skipRight):
                    return True
                else:
                    return False
        
        return True