class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        elif len(stones) == 1:
            return stones[0]
        heapq.heapify(stones)
        nums = []
        while len(stones) > 2:
            nums.append(heapq.heappop(stones))
        
        nums.append(abs(stones[0] - stones[1]))
        return self.lastStoneWeight(nums)
        
