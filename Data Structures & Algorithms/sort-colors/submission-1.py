class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0]*3

        for num in nums:
            count[num] += 1

        k = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[k] = i
                k += 1

        