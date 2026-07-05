class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append([v,w])

        minTime = -1

        minHeap = [[0,k]]
        shortest = set()

        while minHeap:
            wt,des = heapq.heappop(minHeap)
            if des in shortest:
                continue
            shortest.add(des)
            minTime = max(minTime, wt)

            for v,w in adj[des]:
                if v not in shortest:
                    heapq.heappush(minHeap,[w + wt,v])


        for i in range(1,n+1):
            if i not in shortest:
                return -1 
        return minTime
        