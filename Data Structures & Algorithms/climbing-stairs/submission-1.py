class Solution:
    def climbStairs(self, n: int) -> int:
        
        # in dp there is a recursive relationship
        # in this case we start at the n and at each i we have 2 choices
        # step back 2 steps or 1. 
        # once we reach index 0 = that becomes a way
        # if we overshot idx < 0 - return 0 - not a valid way
        memo = {}

        def dp(i: int):
            if i == 0:
                return 1
            
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)
