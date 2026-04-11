class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        minCost = [0]*(n+1)

        minCost[0] = cost[0]
        minCost[1] = cost[1]
        
        for i in range(2,n+1):
            if i < n:
                minCost[i] = cost[i] + min(minCost[i-1],minCost[i-2])
            else:
                minCost[i] = min(minCost[i-1],minCost[i-2])

        return minCost[n]
        