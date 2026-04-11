class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = float('-inf')

        left = 0
        right = len(heights) - 1

        while left < right:
            calArea = min(heights[left], heights[right]) * (right - left)
            area = max(calArea, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return area

         