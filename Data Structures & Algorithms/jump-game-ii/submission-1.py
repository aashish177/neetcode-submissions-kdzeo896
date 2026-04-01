class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        steps = 0
        current_end = 0
        for position in range(len(nums)-1):
            jump = nums[position]
            max_reach = max(max_reach, position+jump)

            if current_end == position:
                current_end = max_reach
                steps += 1
        return steps