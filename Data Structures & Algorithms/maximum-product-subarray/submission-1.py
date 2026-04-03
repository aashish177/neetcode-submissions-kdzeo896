class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = float('-inf')
        for i in range(len(nums)):
            total = nums[i]
            res = float('-inf')
            for j in range(i+1, len(nums)):
                total = total * nums[j]
                res = max(res, total)
            highest = max(res, highest, nums[i])
        return highest