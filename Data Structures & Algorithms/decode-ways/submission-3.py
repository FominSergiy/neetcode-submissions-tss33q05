class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(i: int) -> int:
            if i == n:
                return 1
            
            # nothing can be done with 0 as starting point
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            res = dp(i + 1)
            # check if i, i + 1 are is also valid
            if i < n - 1:
                if (
                    s[i] == "1" or
                    (s[i] == "2" and s[i + 1] < "7")
                ):
                    res += dp(i + 2)
            memo[i] = res
            return memo[i]
    
        return dp(0)