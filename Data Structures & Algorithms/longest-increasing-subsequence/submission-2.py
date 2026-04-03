class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        final_max = 1
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            maximum = 1
            if i == len(nums)-1:
                return 1
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    maximum = max(maximum, 1 + dfs(j))
            cache[i] = maximum
            return maximum
        
        for n in range(len(nums)):
            final_max = max(final_max, dfs(n))
        
        return final_max