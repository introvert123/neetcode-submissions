class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums) #arranges elements in a min Heap
        while len(self.nums) > k: #we only need the top k elements to get the kth Largest
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.nums,val)
        while len(self.nums) > self.k: #we only need the top k elements to get the kth Largest
            heapq.heappop(self.nums)
        return self.nums[0]
        
