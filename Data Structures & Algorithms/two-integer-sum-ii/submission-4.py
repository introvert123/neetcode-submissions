class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        left_ptr = 0
        right_ptr = n - 1

        while left_ptr < right_ptr:
            sum = numbers[left_ptr] + numbers[right_ptr]
            if target == sum:
                return [left_ptr + 1, right_ptr + 1]
            elif sum > target:
                right_ptr -= 1
            else:
                left_ptr += 1
