class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        
        # about having 2 choices
        # base - exit
        # if zero skip
        # otherwise take this char
        # try to do char + 1 if fits the criteria
        def dp(i: int) -> int:
            if i >= n:
                return 1
            
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            ways = dp(i + 1)
            if i + 1 < n:
                if (
                    s[i] == "1" or
                    (s[i] == "2" and s[i + 1] < "7")
                ):
                    ways += dp(i + 2)
            
            memo[i] = ways
            return memo[i]
        
        return dp(0)