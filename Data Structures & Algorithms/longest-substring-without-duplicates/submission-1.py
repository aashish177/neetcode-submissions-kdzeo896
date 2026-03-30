class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxCount = 0
        for i in range(len(s)):
            c = s[i]
            j = i+1
            uniqueSet = set()
            uniqueSet.add(c)
            print(uniqueSet)
            while j < len(s):
                if s[j] not in uniqueSet:
                    uniqueSet.add(s[j])
                    j += 1
                else:
                    break
            count = len(uniqueSet)
            maxCount = max(count, maxCount)
        return maxCount
