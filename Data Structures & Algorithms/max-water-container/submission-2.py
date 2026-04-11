class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        i = 0
        j = n - 1
        maxarea = 0

        while i < j:
            calArea = (j - i) * min(heights[i], heights[j])
            maxarea = max(maxarea, calArea)
            if heights[i] < heights[j]:
                i = i + 1
            else:
                j = j - 1
        
        return maxarea
            
        

        