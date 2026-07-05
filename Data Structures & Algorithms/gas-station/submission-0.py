class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) - sum(cost) < 0: #not possible to go through the circle
            return -1

        #there exists only one solution
        total = 0
        startIdx = 0

        for i in range(len(gas)):

            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                startIdx = i + 1
        
        return startIdx