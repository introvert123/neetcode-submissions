class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) >= 2:
            firstVal = heapq.heappop(stones)
            secVal = heapq.heappop(stones)

            heapq.heappush(stones, firstVal - secVal)
        
        return abs(stones[0])
        
