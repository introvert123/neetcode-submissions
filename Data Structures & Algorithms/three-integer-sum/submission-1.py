class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j = j + 1
                elif total > target:
                    k = k - 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1

                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1

                    while k > 0 and nums[k] == nums[k+1]:
                        k = k - 1

        return triplets


        