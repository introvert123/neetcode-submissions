class KthLargest:
    #Heap = I need quick access to the smallest or largest element repeatedly
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        if len(nums) <= k: 
            self.minHeap = nums
            heapq.heapify(self.minHeap)
        else:
            self.minHeap = nums[:k]
            heapq.heapify(self.minHeap) #arranges elements in a min Heap
            for i in range(k,len(nums)): #we only need the top k elements to get the kth Largest
                if nums[i] > self.minHeap[0]:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap,nums[i])

        
        

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap,val)
        else:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap,val)

        return self.minHeap[0]
        
