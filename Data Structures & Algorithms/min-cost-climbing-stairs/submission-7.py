class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(n):
            if n in cache:
                return cache[n]
            if n > len(cost)-1:
                return 0
            cache[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return cache[n]
        return min(dfs(0), dfs(1))

        