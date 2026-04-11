class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = 1
        dict1 = [1]*len(nums)
        i = 0
        while i < len(nums):
            dict1[i] = lp
            lp = lp * nums[i]
            i += 1
        
        dict2 = [1]*len(nums)
        rp = 1
        j = len(nums) - 1
        while j >= 0:
            dict2[j] = rp
            rp = rp * nums[j]
            j -= 1

        res = [1]*len(nums)
        
        for k in range(len(dict1)):
            res[k] = dict1[k] * dict2[k]

        return res
        