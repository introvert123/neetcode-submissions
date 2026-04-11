class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        list1 = []

        for i in range(len(nums)):
            dict1[nums[i]] = i
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict1 and i != dict1[val]:
                list1.append(i)
                list1.append(dict1[val])
                return list1
        
        return list1
                
        