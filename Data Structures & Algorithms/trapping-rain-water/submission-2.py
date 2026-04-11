class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = 0
        right = n - 1

        maxTrap = 0
        # we have to find min of leftMax and rightMax

        leftMax = height[0]
        rightMax = height[n-1]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                maxTrap = maxTrap + leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxTrap = maxTrap + rightMax - height[right]
                
                

        return maxTrap





        