class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        n = len(s)
        for i in range(n):
            #odd palindromes
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            #odd palindromes
            l,r = i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count