class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [0] * n

        for i in range(n):
            if seen[nums[i]] == 0:
                seen[nums[i]] = 1
            else:
                return nums[i]
        
        