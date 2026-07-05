class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        minHeap = []
        for n1,n2 in points:
            dist = n2*n2 + n1*n1
            minHeap.append([dist,n1,n2])

        heapq.heapify(minHeap)

        while len(res) != k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res