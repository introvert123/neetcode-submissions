class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right)//2

            if nums[mid] == target:
                return True
            elif nums[left] < nums[mid]: #left portion sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # left and mid are equal, can't help but let go of left(duplicate) and move it to ahead to search
                left += 1

        return False


