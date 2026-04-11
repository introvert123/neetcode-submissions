class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # the idea is TO REVERSE THE ARRAY, and take first k elements - reverse
        # also take len - k elements - reverse them
        k = k % len(nums)
        l = 0
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = 0
        r = k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = k
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



        