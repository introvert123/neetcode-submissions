class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        seen = [False]*len(nums)

        def dfs():

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):

                if seen[i]:
                    continue
                
                subset.append(nums[i])
                seen[i] = True
                dfs()

                subset.pop()
                seen[i] = False

        dfs()
        return res
        