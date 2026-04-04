class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 10 20 20 40 0 0
        # 1 2
        # nums1[i], nums2[i], nums[m+i] - 10, 1
        
        # 1, 20, 20, 40, 10, 0
        # 20, 2, 0

        # 1, 2, 20, 40, 10, 10

        # nums2[m-1] - 2
        #             

        
        for i in range(n):
            val2 = nums2[i]
            nums1[m+i] = val2
        
        nums1.sort()

