class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adjList = defaultdict(list)

        for i in range(len(edges)):
            adjList[edges[i][0]].append([edges[i][1],succProb[i]])
            adjList[edges[i][1]].append([edges[i][0],succProb[i]])

        minHeap = [[-1,start_node]]
        best = [0.0]*n
        best[start_node] = 1.0


        while minHeap:
            prob, node = heapq.heappop(minHeap)
            currProb = -prob

            if currProb < best[node]:
                continue
            if node == end_node:
                return abs(prob)

            for n, p in adjList[node]:
                newProb = currProb * p

                if newProb > best[n]:
                    best[n] = newProb
                    heapq.heappush(minHeap, (-newProb, n))
            


        return 0.0