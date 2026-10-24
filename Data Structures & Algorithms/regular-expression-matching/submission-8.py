class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        # remember in terms of match
        # base if we both are used
        # also if end of p and not s return false
        def dp(i: int, j: int) -> bool:
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            memo[(i, j)] = False
            # check for special
            if j + 1 < len(p) and p[j + 1] == "*":
                # do nothing or try to match
                can = dp(i, j + 2)
                can |= (match and dp(i + 1, j))
                memo[(i, j)] |= can
            
            if match:
                memo[(i, j)] |= dp(i + 1, j + 1)
            
            return memo[(i, j)]
        
        return dp(0, 0)
            

            
                
        