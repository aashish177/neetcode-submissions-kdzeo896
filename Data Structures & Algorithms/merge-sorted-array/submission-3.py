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

        
        pointer = m+n-1
        p1 = m-1
        p2 = n-1
        while p1 > -1 and p2 > -1:
            val1 = nums1[p1]
            val2 = nums2[p2]
            if val1 >= val2:
                nums1[pointer] = val1
                p1 -= 1
            else:
                nums1[pointer] = val2
                p2 -= 1
            pointer -= 1
        while p2 > -1:
            nums1[p2] = nums2[p2]
            p2 -= 1



