class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        map = {}
        maxLength = 0
        length = 0
        i = 0
        start = 0
        while i < n:
            if s[i] not in map:
                length = length + 1
            elif s[i] in map and map[s[i]] < start:
                # Character seen before, but OUTSIDE the current window
                length = length + 1
            elif s[i] in map:
                # Character seen INSIDE the current window (duplicate)
                maxLength = max(maxLength, length)
                length = i - map[s[i]]
                start = map[s[i]] + 1

            map[s[i]] = i
            i += 1
        return max(maxLength, length)