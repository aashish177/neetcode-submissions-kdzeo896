class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # iterate over points
        # calculate each euclidean distance
        # map d to point
        # put the keys to priority queue
        # pop k from heap

        maxHeap = []
        res = []
        for i in range(len(points)):
            x, y = points[i]
            dist = (x**2) + (y**2)
            heapq.heappush(maxHeap, [dist, (x, y)])
        
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        return res
