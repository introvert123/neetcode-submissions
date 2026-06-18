class Solution:
    def climbStairs(self, n: int) -> int:

        #O(1) solution

        if n == 1:
            return 1
        
        one = 1
        two = 2 # from 0 and from 1

        for i in range(3,n+1):
            temp = two
            two = two + one #new step could be reached from prev 2 steps - this becomes new two
            one = temp
        return two
