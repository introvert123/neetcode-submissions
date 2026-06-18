class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #Why curMin matters: If the current number is negative, multiplying it with curMin might produce a new maximum.

        currMax, currMin = 1,1
        res = nums[0]

        for num in nums:

            tmp = num * currMax #as currMax is going to be modified, we are storing
            currMax = max(num * currMax, num * currMin, num) #[-1,8] at 8 case
            currMin = min(tmp, num * currMin, num)
            res = max(res,currMax)
        return res
        