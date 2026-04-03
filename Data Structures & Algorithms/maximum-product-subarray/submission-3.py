class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arrHighest = float('-inf')
        for i in range(len(nums)):
            product = nums[i]
            localHighest = float('-inf')
            for j in range(i+1, len(nums)):
                product = product * nums[j]
                localHighest = max(localHighest, product)
            arrHighest = max(localHighest, arrHighest, nums[i])
        return arrHighest