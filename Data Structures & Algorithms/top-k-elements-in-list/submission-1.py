class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for n in nums:
            hMap[n] = hMap.get(n, 0) + 1
        print(hMap)
        
        heap = []
        for key in hMap.keys():
            heapq.heappush(heap, (hMap[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        
        res = []
        for i in range(k):
            val = heapq.heappop(heap)[1]
            res.append(val)

        return res
