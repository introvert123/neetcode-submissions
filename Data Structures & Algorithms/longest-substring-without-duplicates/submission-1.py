class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        map = {}
        maxLength = 0
        length = 0
        i = 0
        while i < n:
            if s[i] not in map:
                length = length + 1
                map[s[i]] = i
                i += 1
            else:
                maxLength = max(maxLength, length)
                length = 0
                i = map[s[i]] + 1
                map = {}

        return max(maxLength, length)