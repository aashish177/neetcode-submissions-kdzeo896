class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
        print(minHeap)
        for _ in range(len(nums)-k):
            print(heapq.heappop(minHeap))
        return minHeap[0]
