class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hMap = {}

        for s in strs:
            countC = [0] * 26
            for c in s:
                countC[ord(c) - ord('a')] += 1
            key = tuple(countC)
            val = hMap.get(key, [])
            val.append(s)
            hMap[key] = val
        
        return list(hMap.values())


                         
