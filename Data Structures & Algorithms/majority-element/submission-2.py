class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyre Moore algo
        count = res = 0

        for num in nums:
            if count == 0:
                res = num
                count += 1
            elif num == res:
                count += 1
            else:
                count -= 1
        
        return res