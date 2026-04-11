class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #quick select algo - O(n) - avg case
        target_idx = len(nums) - k

        def quickSelect(l,r):

            pivot_idx = l #this will be stopped at the place where the pivot > nums[i]
            pivot = nums[r]

            for i in range(l,r):
                if nums[i] <= pivot:
                    # by this, we go through the entire array and move the elements less than p to left
                    nums[pivot_idx], nums[i] = nums[i], nums[pivot_idx]
                    pivot_idx += 1

            #swap the pivot with the index at which a greater value is found    
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            if pivot_idx == target_idx:
                return nums[pivot_idx]
            elif target_idx > pivot_idx:
                return quickSelect(pivot_idx + 1, r)
            else:
                return quickSelect(l, pivot_idx - 1)

        return quickSelect(0, len(nums) - 1)    


        