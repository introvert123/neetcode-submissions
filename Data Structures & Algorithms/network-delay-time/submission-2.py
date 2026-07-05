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


        return minTime if len(shortest) == n else -1
        