class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(0, i+1):
                if dp[j] and s[j:i+1] in wordSet:
                    dp[i+1] = True
                    break
        print(dp)
        return dp[-1]