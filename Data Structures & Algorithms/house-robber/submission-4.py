class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        maxRob = [0]*n
        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0], nums[1])
        for i in range(2,n):
            maxRob[i] = max(nums[i] + maxRob[i-2],maxRob[i-1])
        
        return maxRob[n-1]