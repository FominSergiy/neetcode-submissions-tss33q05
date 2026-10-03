from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TOP DOWN
        n = len(nums)
        memo = {}
        def dp(i: int, amt: int) -> int:
            if i == n:
                return 1 if amt == target else 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            ways = dp(i + 1, amt + nums[i])
            ways += dp(i + 1, amt - nums[i])

            memo[(i, amt)] = ways
            return memo[(i, amt)]
        
        return dp(0, 0)


        # BOTTOM UP
        # n = len(nums)
        # dp = [defaultdict(int) for _ in range(n + 1)]
        # dp[0][0] = 1

        # for i in range(n):
        #     for total, cnt in dp[i].items():
        #         dp[i + 1][total - nums[i]] += cnt
        #         dp[i + 1][total + nums[i]] += cnt
        
        # return dp[n][target]

        # # for i in range(n):
        # #     for total, cnt in dp[i].items():
        # #         dp[i + 1][total - nums[i]] += cnt
        # #         dp[i + 1][total + nums[i]] += cnt
        
        # # return dp[n][target]