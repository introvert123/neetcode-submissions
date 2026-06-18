class Solution:
    def longestPalindrome(self, s: str) -> str:

        #every palindrome has a center
        #odd ones - have one
        #even ones - have two
        #there could be 2n centers

        res = ""
        res_len = 0
        n = len(s)

        for i in range(n):
            #odd len palindrome
            l,r = i,i

            while l >= 0 and r < n and s[l] == s[r]:
                if r + 1 - l > res_len:
                    res = s[l:r+1]
                    res_len = r + 1 - l
                l -= 1
                r += 1

            #even lenth palindrome
            l,r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r + 1 - l > res_len:
                    res = s[l:r+1]
                    res_len = r + 1 - l
                l -= 1
                r += 1
        
        return res





        