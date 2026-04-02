class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = {}
        cache2 = {}
        nums1 = nums[1:]
        nums2 = nums[:len(nums)-1]
        
        if len(nums)==0:
            return 0

        if len(nums)==1:
            return nums[0]

        def dfs1(i):
            if i in cache1:
                return cache1[i]
            
            if i >= len(nums1):
                return 0
            cache1[i] = max(nums1[i]+dfs1(i+2), dfs1(i+1))
            return cache1[i]
        
        def dfs2(i):
            if i in cache2:
                return cache2[i]
            
            if i >= len(nums2):
                return 0
            cache2[i] = max(nums2[i]+dfs2(i+2), dfs2(i+1))
            return cache2[i]

        return max(nums1[0]+dfs1(2), dfs1(1), nums2[0]+dfs2(2), dfs2(1))