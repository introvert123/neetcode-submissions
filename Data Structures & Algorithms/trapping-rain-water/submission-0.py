class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = [0]*n
        maxNum = 0

        for i in range(n):
            if maxNum > left[i]:
                left[i] = maxNum
            maxNum = max(maxNum, height[i])

        j = n - 1
        right = [0]*n
        maxNum = 0
        while j >= 0:
            if maxNum > right[j]:
                right[j] = maxNum
            maxNum = max(maxNum, height[j])
            j -= 1

        maxTrap = 0
        for i in range(n):
            if left[i] != 0 and right[i] != 0:
                val = min(left[i],right[i]) - height[i]
                if val >= 0:
                    maxTrap = maxTrap + val

        return maxTrap



        