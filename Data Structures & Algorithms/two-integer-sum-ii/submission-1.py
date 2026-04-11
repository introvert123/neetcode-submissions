class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}
        res = []
        for i in range(len(numbers)):
            dict1[numbers[i]] = i + 1
        
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in dict1:
                res.append(i + 1)
                res.append(dict1[num])
                return res
            
            

        