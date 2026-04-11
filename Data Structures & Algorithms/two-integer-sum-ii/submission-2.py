class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}
        
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in dict1:
                return [dict1[num], i + 1]
            else:
                dict1[numbers[i]] = i + 1  
            
            

        