class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cache = {}
        # def dfs(total):
        #     res = float('inf')
        #     if total == amount:
        #         return 0
        #     if total > amount:
        #         return res
        #     if total in cache:
        #         return cache[total]

        #     for c in coins:
        #         res = min(res, dfs(total+c)+1)
            
        #     cache[total] = res
        #     return cache[total]
        
        # change = dfs(0)
        # return change if change < float('inf') else -1

        # dp = {total: -1}
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[amount] if dp[amount] != float('inf') else -1

            
