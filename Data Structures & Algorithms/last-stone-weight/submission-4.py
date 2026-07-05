class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapify always result into minHeap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            top1 = -heapq.heappop(maxHeap)
            top2 = -heapq.heappop(maxHeap)
            if top1 > top2:
                heapq.heappush(maxHeap,top2-top1)

        return 0 if len(maxHeap) == 0 else -maxHeap[0]