class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        adjList = [[] for _ in range(n+1)]

        for i in range(len(trust)):
            adjList[trust[i][0]].append(trust[i][1])

        potential = float('inf')
        for i in range(1,n+1):
            if len(adjList[i]) == 0:
                potential = i
        
        if potential == float('inf'):
            return -1
        else:
            for i in range(1,n+1):
                if i != potential and potential not in adjList[i]:
                    return -1
        return potential
        
        
        