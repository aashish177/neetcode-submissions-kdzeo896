class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3, 4, 5, 6, 1, 2]
        # [6, 1, 2, 3, 4, 5]
        # [1, 2, 3, 4, 5, 6]

        # l=0, r=5

        # t=1, 
        # if nums[l] > nums[r],  we know its not sorted
        # m = (l+r)//2
        # if nums[m] > nums[l], we know that nums[l:m] is sorted
        #   else, we know that nums[l:m] is not sorted
        # if nums[m] > target -> we want to get smaller side (compare nums[l], nums[r])
        # if nums[m] < target -> we want to get to larger side (compare nums[l], nums[r])

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # sorted
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1