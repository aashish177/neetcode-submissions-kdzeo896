class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # dp = [False] * (len(s)+1)
        # dp[0] = True
        # for i in range(len(s)):
        #     for j in range(0, i+1):
        #         if dp[j] and s[j:i+1] in wordSet:
        #             dp[i+1] = True
        #             break
        # print(dp)
        # return dp[-1]
        wordSet = set(wordDict)
        cache = {}
        def backtrack(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and backtrack(j):
                    cache[j] = True
                    return cache[j]
            cache[i] = False
            return False
        
        return backtrack(0)