class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for n in nums:
            hMap[n] = hMap.get(n, 0) + 1
        print(hMap)
        
        # Use a list of tuples to handle duplicate frequencies and allow sorting
        swapped_map = [(v, k) for k, v in hMap.items()]

        # Sort based on frequency in descending order
        sorted_val = sorted(swapped_map, reverse=True)
        print(sorted_val)

        res = []
        for n in range(k):
            res.append(sorted_val[n][1])
        
        return res
