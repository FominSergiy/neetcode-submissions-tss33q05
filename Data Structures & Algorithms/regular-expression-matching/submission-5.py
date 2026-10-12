class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        # remember in terms of match
        # base if we both are used
        # also if end of p and not s return false

        def dp(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            memo[(i, j)] = False
            # check for regular exp
            if j + 1 < len(p) and p[j + 1] == "*":
                # 2 choices
                skip = dp(i, j + 2)
                try_match = match and dp(i + 1, j)
                memo[(i, j)] |= skip or try_match
            
            if match:
                memo[(i, j)] |= dp(i + 1, j + 1)
            
            return memo[(i, j)]
        
        return dp(0, 0)
                
                
        