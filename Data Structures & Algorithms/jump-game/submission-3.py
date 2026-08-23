class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n

        # DO DFS SOLUTION NEXT TIME HERE !!

        # pick n - 1 as a goal,
        # go backwards and update the goal as long as it is within the range
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return True if goal == 0 else False