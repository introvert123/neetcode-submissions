class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        arr = [True]*n

        for i in range(n-2,-1,-1):
            if nums[i] == 0:
                arr[i] = False
            else:
                if True in arr[i+1:i+nums[i]+1]:
                    arr[i] = True
                else:
                    arr[i] = False
        
        return arr[0]
        