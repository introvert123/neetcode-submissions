class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        def dfs(i, numSum):

            if numSum == target:
                res.append(subset.copy())
                return

            if numSum > target or i >= len(nums):
                return 

            subset.append(nums[i])
            dfs(i, numSum + nums[i])

            subset.pop()
            dfs(i+1, numSum)

        dfs(0,0)
        return res

        