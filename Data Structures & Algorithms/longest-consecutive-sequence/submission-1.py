class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 1
        n = len(nums)
        if n == 0:
            return 0
        num = nums[0]
        i = 0
        nums.sort()
        
        while i < n:
            k = 1
            j = 0
            num = nums[i]
            while j < n:
                if (num + 1 == nums[j]):
                    num = nums[j]
                    k += 1
                j += 1
            if k > maxLen:
                maxLen = k
            i += 1

        return maxLen
            

        