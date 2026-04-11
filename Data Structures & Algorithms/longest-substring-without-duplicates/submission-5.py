class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        left = 0
        right = 0
        map = {}

        maxLen = 0
        length = 0

        while right < n:
            if s[right] not in map:
                length += 1   
            else:
                if map[s[right]] >= left:
                    maxLen = max(maxLen,length)
                    length = right - map[s[right]]
                    left = map[s[right]] + 1 #updating the window
                else:
                    length += 1
            
            map[s[right]] = right #updating the map with new index     
            right += 1

        return max(maxLen, length)
                
        