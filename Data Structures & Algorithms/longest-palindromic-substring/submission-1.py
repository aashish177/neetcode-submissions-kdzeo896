class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = s[0]
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         subString = s[i:j+1]
        #         found = True
        #         l, r = 0, len(subString)-1
        #         while l < r:
        #             if subString[l] != subString[r]:
        #                 found = False
        #             l += 1
        #             r -= 1
        #         if found:
        #             if len(subString)>len(res):
        #                 res = subString
        # return res
        res = ""
        def check(l, r):
            if l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+= 1
                return check(l, r)
            return s[l+1:r]   
        
        for i in range(len(s)):
            pal = check(i, i)
            if len(res) < len(pal):
                res = pal
            
            pal = check(i, i+1)
            if len(res) < len(pal):
                res = pal

        return res

        # check if n-1 and n+1 are same - res[n-1]+res[n]+res[n+1], check (n-2) (n+2)
        # or if n and n+1 are same - res[n]+res[n+1]
        # check (n-1) and (n+2)
        # 
        # check
        # if l >= 0 and r < len(s)
        # check if n[l] == n[r]
        # val = n[l] + val + n[r]
        # if so, res[l-1], res[r+1]


        # check(l, r, val)
        # if l < 0 or r >= len(s)
        # return val
        # if s[l] == s[r]
        # check (l-1, r+1) 