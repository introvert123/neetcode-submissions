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
                val = leftMax - height[left]
                if val>=0:
                    maxTrap = maxTrap + val
                leftMax = max(leftMax, height[left])
                
            else:
                right -= 1
                val = rightMax - height[right]
                if val>=0:
                    maxTrap = maxTrap + val
                rightMax = max(rightMax, height[right])
                

        return maxTrap





        