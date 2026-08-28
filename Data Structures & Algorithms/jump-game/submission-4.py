class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DO DFS SOLUTION NEXT TIME HERE !!
        # another nother next time

        n = len(nums) - 1
        goal = n

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return True if goal == 0 else False
