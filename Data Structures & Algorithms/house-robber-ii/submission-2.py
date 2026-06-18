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
            maxRob = [0]*size
            maxRob[0] = sub[0]
            maxRob[1] = max(sub[0],sub[1])
            for i in range(2,size):
                maxRob[i] = max(maxRob[i-2] + sub[i], maxRob[i-1])
            
            return maxRob[size - 1]

        return max(houseRobber(nums[:n-1]),houseRobber(nums[1:n]))

            





        