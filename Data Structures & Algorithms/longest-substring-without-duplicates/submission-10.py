class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLen = 0
        map1 = {}

        left = 0
        right = 0

        while right < len(s):
            if s[right] in map1 and map1[s[right]] >= left:
                left = map1[s[right]] + 1
            
            maxLen = max(maxLen, right - left + 1)
            map1[s[right]] = right
            right += 1
            

        return maxLen