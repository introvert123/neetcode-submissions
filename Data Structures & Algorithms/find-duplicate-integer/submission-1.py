class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # Since every value is between 1 and n, 
        # each number corresponds to an index in the array (num - 1).
        # if num = 4, index 4 will not exist, which is why we consider num-1
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        
        return -1

        
        
        