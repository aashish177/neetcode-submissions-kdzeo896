class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1
        while r<len(s2):
            reqStr = s2[l:r+1]
            print(reqStr)
            hMap1 = {}
            hMap2 = {}
            for i in range(r-l+1):
                hMap1[s1[i]] = 1 + hMap1.get(s1[i], 0)
                hMap2[reqStr[i]] = 1 + hMap2.get(reqStr[i], 0)
            if hMap1 == hMap2:
                print(hMap1)
                print(hMap2)
                return True
            l += 1
            r += 1
        return False
