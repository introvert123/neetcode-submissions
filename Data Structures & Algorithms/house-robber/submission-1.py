class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        maxRob = [0]*n
        maxRob[0] = nums[0]
        maxRob[1] = nums[1]
        if n == 2:
            return max(nums[0], nums[1])
        maxRob[2] = nums[2] + maxRob[0]
        maxAmt = max(nums[0], nums[1], maxRob[2])
        

        for i in range(3,n):
            maxRob[i] = max(nums[i] + maxRob[i-2], nums[i] + maxRob[i-3])
            maxAmt = max(maxAmt, maxRob[i])
       
        return maxAmt