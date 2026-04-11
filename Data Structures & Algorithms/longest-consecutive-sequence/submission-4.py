class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 1
        n = len(nums)
        if n == 0:
            return 0
        s = set()
        for i in range(n):
            s.add(nums[i])
            
        i = 0
        while i < n:
            num = nums[i]
            if num - 1 not in s:
                k = 1
                while num + 1 in s:
                    k+=1
                    num = num + 1
                if k > maxLen:
                    maxLen = k
            i += 1

        return maxLen
            

        