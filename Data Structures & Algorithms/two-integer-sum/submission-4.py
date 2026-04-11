class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        list1 = []
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict1:
                list1.append(dict1[val])
                list1.append(i)
                return list1
            dict1[nums[i]] = i
        
        return list1
                
        