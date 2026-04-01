class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        contiguos = 0
        maxSum = float('-inf')
        addition = 0

        for n in nums:
            print("contiguos ", contiguos)
            print("n ", n)
            addition = contiguos + n
            print("addition ", addition)
            contiguos = contiguos + n
            maxSum = max(n, contiguos, maxSum)
            if addition < 0:
                contiguos = 0
            print("maxSum ", maxSum)
            print("_______")
        return maxSum