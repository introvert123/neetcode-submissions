class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0]*3

        for num in nums:
            count[num] += 1

        k = i = 0
        while i < len(nums):
            j = 0
            while j < count[k]:
                nums[i] = k
                j += 1
                i += 1
            k += 1

        