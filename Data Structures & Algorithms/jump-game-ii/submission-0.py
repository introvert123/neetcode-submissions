class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = r = 0 #our window

        while r < len(nums) - 1: # if r reaches len(nums) - 1, we have reached goal
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res