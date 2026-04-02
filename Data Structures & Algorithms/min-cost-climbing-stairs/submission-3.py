class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0 for _ in range(len(cost) + 2)]  
        for i in range(len(cost)-1, -1, -1):
            res[i] = min(cost[i] + res[i+1], cost[i] + res[i+2])
        return min(res[0],res[1])

        