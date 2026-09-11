class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # same flavour as climbing stairs, but now we need to record
        # cost

        # same reason we go with n + 1
        # because we want to know value at n - top of the stairs
        # cant return 

        # for that it makes more sense to move
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )
        return dp[-1]
