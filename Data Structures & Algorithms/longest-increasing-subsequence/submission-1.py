class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = [-1] * n

        # def dp(i: int):
        #     if memo[i] != -1:
        #         return memo[i]
            

        #     LIS = 1 # sub-seq at any idx is 1
        #     # try to build logest sub-seq at this idx
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, dp(j) + 1)
            
        #     memo[i] = LIS
        #     return memo[i]
        
        # # need to consider ALL sub-seq starting at any i
        # return max([dp(i) for i in range(n)])
        n = len(nums)
        dp = [1] * n
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)