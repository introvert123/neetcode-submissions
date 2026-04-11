class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        
        def houseRobber(arr):
            prev2 = 0
            prev1 = 0
            
            for num in arr:
                curr = max(prev1, num + prev2)
                prev2 = prev1
                prev1 = curr
                
            return prev1
        
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))

        


        