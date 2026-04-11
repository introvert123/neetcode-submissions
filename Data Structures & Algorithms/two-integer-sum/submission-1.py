class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        list1 = []

        for i in range(len(nums)):
            dict1[i] = nums[i]
        
        for i in range(len(nums)):
            val = target - nums[i]
            for key,value in dict1.items():
                if value == val and key != i:
                    list1.append(i)
                    list1.append(key)
                    return list1
        
        return list1
                
        