class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        #maxRob[i] = maximum money we can rob from houses 0..i
        maxRob = [0]*n

        #For each house i, the maximum money we can have depends on:
        #Not robbing it → same money as i - 1
        #Robbing it → money at i + best up to i - 2
        
        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0], nums[1])
        for i in range(2,n):
            maxRob[i] = max(nums[i] + maxRob[i-2],maxRob[i-1])
            #rob current house and skip current house
        
        return maxRob[n-1]