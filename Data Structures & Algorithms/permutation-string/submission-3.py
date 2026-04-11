class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = {}
        freq2 = {}

        # count characters of s1
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1

        left = 0
        for right in range(len(s2)):
            # add right character
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1

            # shrink window if too large
            if right - left + 1 > len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1

            # check match
            if freq1 == freq2:
                return True

        return False
