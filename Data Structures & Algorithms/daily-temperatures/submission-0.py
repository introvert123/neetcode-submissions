class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        for i in range(n-1,-1,-1):
            while stack:
                if temperatures[stack[-1]] > temperatures[i]:
                    result[i] = stack[-1] - i
                    break
                else:
                    stack.pop()
            stack.append(i)
        
        return result