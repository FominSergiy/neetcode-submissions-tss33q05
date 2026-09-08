class Solution:
    def rob(self, nums: List[int]) -> int:
        # problem is similar to fib
        # if I start from the end
        # I could have only gotten there from
        # previous house or house 2 blocks down
        # though here is the difference
        # if its previous house, I cannot rob it, but 2 back I can
        # memo = {}
        # def dp(i: int):
        #     # only base case, reached start house
        #     if i == 0:
        #         return nums[i]
            
        #     if i < 0:
        #         # overshot
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
        #     return memo[i]
        
        # return dp(len(nums) - 1)
        # have to use guard if len nums < 2
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        # bottom up
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # print(dp)
        return dp[-1]