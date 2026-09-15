class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # TOP DOWN
        # n = len(nums)
        # memo = [-1] * n

        # def dp(i: int):
        #     if memo[i] != -1:
        #         return memo[i]

        #     LIS = 1
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, dp(j) + 1)
            
        #     memo[i] = LIS
        #     return memo[i]
        
        # return max([dp(i) for i in range(n)])

        # BOTTOM-UP
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)