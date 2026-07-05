class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # the idea is that if a goal could be reached from one point, anything that reaches that point will reach goal
        # we keep shifting the goal
        goal = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False