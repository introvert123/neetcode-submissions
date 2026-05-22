class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #sort numbers first
        nums.sort()

        seen = [False]*len(nums)
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):

                if seen[i]:
                    continue

                #if the num we are gng to see is something we used up previously, it means nothing
                #of the same num should be seen in this branch
                if i > 0 and nums[i] == nums[i-1] and seen[i-1] == False:
                    continue
                
                subset.append(nums[i])
                seen[i] = True
                dfs()

                subset.pop()
                seen[i] = False
                
        
        dfs()
        return res