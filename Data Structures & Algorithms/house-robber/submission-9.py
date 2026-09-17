class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp top dowm first
        # then bottom up

        # # memo = {}
        # def dp(i: int) -> int:
        #     if i == 0:
        #         return nums[0]
            
        #     if i == 1:
        #         return nums[1]

        #     # dont rob this house come from prev
        #     # or rob this house and come from two back            
        #     return max(dp(i - 1), dp(i - 2) + nums[i])

        # return dp(len(nums) - 1)
        if len(nums) == 1:
            return nums[0]
            
        
        # top-down
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
