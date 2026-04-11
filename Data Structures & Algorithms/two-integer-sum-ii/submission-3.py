class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #dict1 = {}
        
        #for i in range(len(numbers)):
            #num = target - numbers[i]
            #if num in dict1:
                #return [dict1[num], i + 1]
            #else:
                #dict1[numbers[i]] = i + 1  
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        

            
            

        