class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subset = []
            for curr in res:
                new_subset.append(curr + [num])
            res.extend(new_subset)
        
        return res