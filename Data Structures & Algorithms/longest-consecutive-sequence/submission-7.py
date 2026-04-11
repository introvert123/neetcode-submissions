class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)

        maxLen = 0

        for num in nums:
            if num-1 not in setNums:
                x = num
                len = 1
                while x+1 in setNums:
                    len += 1
                    x = x+1
                maxLen = max(len, maxLen)

        return maxLen



        