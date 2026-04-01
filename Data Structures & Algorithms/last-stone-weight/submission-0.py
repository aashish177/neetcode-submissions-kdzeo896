class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])
        print(maxHeap)

        while len(maxHeap)>1:
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)
            diff = (val1 - val2)
            heapq.heappush(maxHeap, diff)
        
        return -heapq.heappop(maxHeap) if maxHeap else 0