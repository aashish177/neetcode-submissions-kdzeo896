class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            print(i)
            for j in range(i+1, len(nums)):
                print(j)
                print("---")

                if nums[i] == nums[j]:
                    return True
        return False
        