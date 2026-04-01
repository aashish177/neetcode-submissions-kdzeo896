class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        aMap = {}
        for t in tasks:
            aMap[t] = aMap.get(t, 0) - 1
        maxHeap = list(aMap.values())
        heapq.heapify(maxHeap)
        
        q = collections.deque()

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

