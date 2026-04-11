class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1 = len(word1)
        n2 = len(word2)

        i = j = 0
        res = ""

        while i < n1 and j < n2:
            res = res + word1[i] + word2[j]
            i += 1
            j += 1
        
        while i < n1:
            res = res + word1[i]
            i += 1
        
        while j < n2:
            res = res + word2[j]
            j += 1

        return res
        