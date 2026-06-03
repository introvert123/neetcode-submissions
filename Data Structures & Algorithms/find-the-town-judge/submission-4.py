class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        #incoming = n -1 (every node is pointing to this node)
        #outgoing = 0 (node is pointng to no node)

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for i in range(len(trust)):
            outgoing[trust[i][0]] += 1
            incoming[trust[i][1]] += 1

        for i in range(1,n+1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        
        return -1
        