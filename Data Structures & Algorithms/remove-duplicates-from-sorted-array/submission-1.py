class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != nums[pointer]:
                nums[pointer + 1] = nums[i]
                pointer = pointer + 1
        
        return pointer + 1
        