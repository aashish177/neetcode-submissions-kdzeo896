class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suf = 1
        pref = 1
        n = len(nums)
        maximum = float('-inf')
        for i in range(n):
            if pref == 0: pref = 1
            if suf == 0: suf = 1
            pref = pref*nums[i]
            suf = suf*nums[n-i-1]
            maximum = max(maximum, pref, suf)

        return maximum