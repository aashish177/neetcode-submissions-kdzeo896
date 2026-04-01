class KthLargest:

    # minHeap initialize
    # add to minHeap
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.lim = k
        for n in nums:
            heapq.heappush(self.minHeap, n)
        req = len(nums) - k
        for _ in range(req):
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.lim:
            heapq.heappop(self.minHeap)
        print(self.minHeap)
        
        return self.minHeap[0]
