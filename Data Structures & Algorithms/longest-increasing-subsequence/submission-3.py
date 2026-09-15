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

        # iterate backwards
        # and for each i as start, compare all numbers that are in front of it
        # as long as nums[start] < nums[j]
        # if that is true
        # then dp[i] is a max of already current dp[i] OR value of dp[j] + 1
        # this assumes we either take a num of our existing sequence is already greater than
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # return max since we build answer back to front
        # and max over the dp is what we need at any given num
        return max(dp)