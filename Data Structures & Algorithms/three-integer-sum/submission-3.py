class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        n = len(nums)
        i = 0
        while i < n:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            target = -(nums[i])
            left_ptr = i + 1
            right_ptr = n - 1

            while left_ptr < right_ptr:
                sum = nums[left_ptr] + nums[right_ptr]

                if target == sum:
                    res.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
                    
                    #when we find a pair, tha's when we don't want a similar same pair again so we remove duplicates
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                        left_ptr += 1

                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr + 1]:
                        right_ptr -= 1
                elif sum > target:
                    right_ptr -= 1
                else:
                    left_ptr += 1

                 

            i += 1

        return res

        