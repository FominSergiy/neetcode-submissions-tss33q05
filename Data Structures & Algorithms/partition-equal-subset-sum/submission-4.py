class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        # it has to be a number evenly divisble by 2
        # otherwise there is no way to make 2 equal subsets
        if total % 2 != 0:
            return False
        
        half = total // 2

        # # idea is, 2nd idx is any number before the half - since all stop at half
        # # and we are really just building a half
        # memo = [[None] * (half + 1) for _ in range(n + 1)]
        # def dp(i: int, target: int) -> bool:
        #     if target == 0:
        #         return True
            
        #     if target < 0 or i >= n:
        #         return False
            
        #     if memo[i][target] is not None:
        #         return memo[i][target]
            
        #     # either not take this num
        #     # or take this num
        #     memo[i][target] = dp(i + 1, target) or dp(i + 1, target - nums[i])
        #     return memo[i][target]
            

        # return dp(0, half)
        
        # top down
        target = half
        n = len(nums)
        # for each i we get target + 1 options
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True # means for all subsets not can sum to 0
        
        # we always start from 1 and compare to previous num
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j: # num up to this point have to add up to target j
                    dp[i][j] = (
                        dp[i - 1][j] or 
                        dp[i - 1][j - nums[i - 1]]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]

        
        return dp[n][target]