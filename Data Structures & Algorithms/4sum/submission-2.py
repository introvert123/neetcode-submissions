class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        i = 0
        res = []
        n = len(nums)

        while i < n:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            targetSum = target - nums[i]
            j = i + 1
            while j < n:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                t = targetSum - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[left] + nums[right]
                    if t == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif t > sum:
                        left += 1
                    else:
                        right -= 1

                j += 1
            i += 1

        return res