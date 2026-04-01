class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for position, jump in enumerate(nums):
            if max_reach < position:
                return False
            jump = nums[position]
            currMaxReach = position + jump
            max_reach = max(currMaxReach, max_reach)
        return True
              

             

