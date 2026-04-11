class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        heap = []
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            heap.append((dist,[point[0], point[1]]))
        
        heapq.heapify(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res