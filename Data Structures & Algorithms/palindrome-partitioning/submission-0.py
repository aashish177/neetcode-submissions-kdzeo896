class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        def dfs(i):
            if i >= len(s):
                res.append(parts.copy())
                return
        
            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()

        dfs(0)
        return res

    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    
        
            
            
        
