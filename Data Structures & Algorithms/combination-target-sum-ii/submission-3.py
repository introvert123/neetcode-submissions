class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        subset = []
        def dfs(i,numSum):

            if numSum == target:
                res.append(subset.copy())
                return

            if numSum > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i+1, numSum + nums[i])

            subset.pop()
            
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1,numSum)

    
        dfs(0,0)
        return res

        