class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = set()
        for i in range(len(sorted_nums)):
            val = sorted_nums[i]
            l, r = i+1, len(sorted_nums)-1
            while l < r:
                total = sorted_nums[l] + sorted_nums[r] + val
                print(total)
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.add((sorted_nums[l], sorted_nums[r], val))
                    print(res)
                    l += 1
                    r -= 1
                    # # while l<r and nums[l] == nums[l+1]:
                    # #     l+=1
                    # while l<r and nums[r] == nums[r-1]:
                    #     r -= 1
        
        return list(res)