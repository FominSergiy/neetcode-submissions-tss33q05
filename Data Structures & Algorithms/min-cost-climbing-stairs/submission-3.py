class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # same flavour as climbing stairs, but now we need to record
        # cost

        # for that it makes more sense to move 
        memo = {}

        def dp(i: int):
            # if overshot its zero
            # else costs will add up and that will be the answer
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i + 1), dp(i + 2)) + cost[i]
            return memo[i]
        
        # start from either 1st cell or 2nd cell
        return min(dp(0), dp(1))
        # tabular
        # n = len(cost)
        # dp = [0] * (n + 1)
        # for i in range(2, n + 1):
        #     dp[i] = min(
        #         dp[i - 1] + cost[i - 1],
        #         dp[i - 2] + cost[i - 2]
        #     )
        # return dp[n] 
