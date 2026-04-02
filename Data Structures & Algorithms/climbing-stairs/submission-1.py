class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}
        def dfs(i):
            res = 0
            if i in cache:
                return cache[i]
            if i==n:
                return 1
            if i>n:
                return 0
            for j in range(i+1, i+3):
                res += dfs(j)
                cache[j] = res
            return res
    
        return dfs(0)