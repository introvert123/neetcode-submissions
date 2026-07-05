class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""
        if len(s) < len(t):
            return ""

        resLen = float('inf') #need to find the smallest substring possible
        res = [0,0] #we need to record the l and r so that we can return the substring

        countS,countT = {},{}
        have = need = 0

        for c in t:
            countT[c] = countT.get(c,0) + 1

        need = len(countT)

        l = r = 0
        while r < len(s):
            countS[s[r]] = 1 + countS.get(s[r],0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while need == have:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1


        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""
        