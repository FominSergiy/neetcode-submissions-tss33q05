class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DO DFS SOLUTION NEXT TIME HERE !!
        # another nother next time
        goal = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0