class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # same flavour as climbing stairs, but now we need to record
        # cost

        # same reason we go with n + 1
        # because we want to know value at n - top of the stairs
        # we need to go past last idx n - 

        # for that it makes more sense to move
        n = len(cost)
        dp = [0] * (n + 1)
        # I could have gotten to i either by stepping from 1 step and paying cost there
        # or stepping from 2 step and paying cost there - whichever is the smallest is what we take
        for i in range(2, n + 1): # just a bit past the last step
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )
        
        return dp[-1]
