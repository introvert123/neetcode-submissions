class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        #the idea is to use the house robber I - run this method on all numbers excluding last | also on all numbers excluding first
        #whatever is max wil be the result - this way we are not using the first and last togther

        if n == 1:
            return nums[0]

        def houseRobber(sub):

            size = len(sub)

            if size == 1:
                return sub[0]
            prev2 = sub[0]
            prev1 = max(sub[0],sub[1])
            for i in range(2,size):
                temp = prev1
                prev1 = max(prev2 + sub[i], prev1)
                prev2 = temp
            
            return prev1

        return max(houseRobber(nums[:n-1]),houseRobber(nums[1:n]))

            





        