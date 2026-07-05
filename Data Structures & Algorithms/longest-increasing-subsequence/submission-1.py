class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i],1 + lis[j])
        
        return max(lis)
        