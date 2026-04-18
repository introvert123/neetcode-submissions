class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map = {}

        start = 0
        end = 0
        maxLen = 0

        while end < len(s):
            if s[end] in map and map[s[end]] >= start:
                start = map[s[end]] + 1
            map[s[end]] = end
            maxLen = max(maxLen, end - start + 1) # everytime we expand we check len
            end += 1

        return maxLen
        