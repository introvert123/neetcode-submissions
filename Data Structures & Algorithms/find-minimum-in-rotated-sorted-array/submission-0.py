class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # in not fully rotated arrays, nums[l] >  nums[r]will be always greater 
            # if not it means it is fully sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            # this below condition means that the left array is sorted
            # eg: 4,5,6,7,0,1,2 (7 > 4) which means left is sorted array
            # If left side is sorted, it contains NO values smaller than nums[l] ignore and search right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # if nums[l] > nums[m] - this means that we have entered the second sorted array
                # and the miniumum is on the left of mid
                # from mid to right - all will be in increasing order only
                r = m - 1
        return res