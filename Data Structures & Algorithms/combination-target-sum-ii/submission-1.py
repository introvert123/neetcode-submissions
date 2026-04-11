class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        subset = []
        def dfs(i,numSum):

            if numSum == target:
                res.append(subset.copy())
                return
            
            if numSum > target or i >= len(candidates):
                return


            subset.append(candidates[i])
            dfs(i+1, numSum + candidates[i])

            subset.pop()

            # if we have made a choice to skip a number, we skip all such numbers as a group
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, numSum)

        dfs(0,0)
        return res




