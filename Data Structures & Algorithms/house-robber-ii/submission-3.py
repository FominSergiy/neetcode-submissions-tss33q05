class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        
        # memo = [[-1] * 2 for _ in range(len(nums))]
        # # perform 2 dp - 1 n
        # def dp(i: int, flag: bool):
        #     if i == 0 and flag:
        #         return nums[0]
        #     elif i <= 0:
        #         return 0
            
        #     if memo[i][flag] != -1:
        #         return memo[i][flag]
            
        #     memo[i][flag] = max(dp(i - 1, flag), dp(i - 2, flag) + nums[i])
        #     return memo[i][flag]
        
        # return max(dp(n - 1, False), dp(n - 2, True))

        # bottom-up
        # split into 2 searches of (1, n - 1) and (0, n - 2)
        # return max of the two
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(
            self.helper(nums[1:]),
            self.helper(nums[:n - 1])
        )
    
    def helper(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
            
            

