class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n

        for i in range(n - 1, -1, -1):
            # print(f"for i:{i}, {nums[i]}")
            if nums[i] + i >= goal:
                # print(f"for i:{i}, {nums[i]}")
                goal = i
        
        return True if goal == 0 else False