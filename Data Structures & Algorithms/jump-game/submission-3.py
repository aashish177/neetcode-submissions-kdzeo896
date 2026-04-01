class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(index):
            if index in cache:
                return cache[index]
            if index >= len(nums)-1:
                return True 
            
            val = nums[index]
            for i in range(val, 0, -1):
                if dfs(index+i):
                    cache[index] = True
                    return True
            cache[index] = False
            return False

        return dfs(0)    

             

