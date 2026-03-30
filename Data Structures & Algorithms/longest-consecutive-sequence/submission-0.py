class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in numSet:
                n = 1
                while (num+n) in numSet:
                    n += 1
                longest = max(longest, n)
        
        return longest
