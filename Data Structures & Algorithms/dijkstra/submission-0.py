class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = defaultdict(list)

        for u,v,w in edges:
            adj[u].append([v,w])
        

        minHeap = [[0,src]]
        shortest = {}

        while minHeap:
            wt,ver = heapq.heappop(minHeap)
            if ver in shortest:
                continue
            shortest[ver] = wt
            for dst,wt2 in adj[ver]:
                if dst not in shortest:
                    heapq.heappush(minHeap,[wt2 + wt,dst]) #wt = weight to reach parent of thsi node

            
        #unconnected nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        
        return shortest