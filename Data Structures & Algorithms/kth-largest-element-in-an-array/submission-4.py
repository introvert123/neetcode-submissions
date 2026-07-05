class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = nums[:k] #maintaining a heap of K elements
        heapq.heapify(minHeap) #O(n)

        for i in range(k,len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])

        
        return minHeap[0]


