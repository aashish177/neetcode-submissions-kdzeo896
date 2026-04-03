# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         parts = []
#         cache = {}

#         def dfs(i):
#             if i in cache:
#                 return cache[i]

#             if i >= len(s):
#                 res.append(parts.copy())
#                 return
        
#             for j in range(i, len(s)):
#                 if self.isPalindrome(i, j, s):
#                     parts.append(s[i:j+1])
#                     dfs(j+1)
#                     parts.pop()

#         dfs(0)
#         return res

#     def isPalindrome(self, l, r, s):
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l+=1
#             r-=1
#         return True
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}

        def dfs(i):
            # If we've already solved for this starting position, return it
            if i in memo:
                return memo[i]
            
            # Base Case: If we reached the end, return a list containing an empty list
            # (This represents one valid way to complete the partition)
            if i == len(s):
                return [[]]

            res = []
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    current_pal = s[i : j + 1]
                    
                    # Recursively get all ways to partition the REST of the string
                    # We combine our current palindrome with every result from the future
                    for rest in dfs(j + 1):
                        res.append([current_pal] + rest)
            
            memo[i] = res
            return res

        return dfs(0)

    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l, r = l + 1, r - 1
        return True
        
            
            
        
