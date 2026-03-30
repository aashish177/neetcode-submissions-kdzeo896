class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hMapS = {}
        hMapT = {}
        for c in s:
            hMapS[c] = hMapS.get(c, 0) + 1
        
        for c in t:
            hMapT[c] = hMapT.get(c, 0) + 1

        print(hMapS)
        print(hMapT)

        return hMapS == hMapT
