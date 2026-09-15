class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        # it has to be a number evenly divisble by 2
        # otherwise there is no way to make 2 equal subsets
        if total % 2 != 0:
            return False
        
        half = total // 2

        # idea is, 2nd idx is any number before the half - since all stop at half
        # and we are really just building a half
        memo = [[None] * (half + 1) for _ in range(n + 1)]
        # print(memo)
        def dp(i: int, target: int) -> bool:
            if target == 0:
                return True
            
            if target < 0 or i >= n:
                return False
            
            if memo[i][target] is not None:
                return memo[i][target]
            
            # either not take this num
            # or take this num
            memo[i][target] = dp(i + 1, target) or dp(i + 1, target - nums[i])
            return memo[i][target]
            

        return dp(0, half)
        