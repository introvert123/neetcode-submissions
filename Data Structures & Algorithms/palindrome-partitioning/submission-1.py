class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def palindrome(substr: str):
            i = 0
            j = len(substr) - 1

            while i<=j:
                if substr[i] == substr[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        def dfs(i):

            if i >= len(s):
                res.append(subset.copy())
                return

            # this loop is for incrementing the size of the substring - level like a, aa, aab
            # runs only when recursion returns
            # recursion goes deep first
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if palindrome(substr) == True:
                    subset.append(substr)
                    dfs(j+1) # this is for rest of the string from j+1 index (eg: aa - substr, from b forms next)
                    subset.pop()
                # if a branch is not a palindrome we move to the next size

        dfs(0)
        return res

#The loop starts a branch
#Recursion goes all the way down
#Only when recursion returns does the loop continue

        
        