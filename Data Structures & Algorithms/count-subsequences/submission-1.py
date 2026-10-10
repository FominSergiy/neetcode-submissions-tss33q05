class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # again, use 2 pointers i j and advance i only when match to j
        # 2 choises - advance or not
        memo = {}

        def dp(i: int, j: int) -> int:
            if j == len(t):
                return 1 #used all chars
            
            if i == len(s):
                return 0 #could not build t
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # skip
            cnt = dp(i + 1, j)
            # if chars match, move both pointers
            if s[i] == t[j]:
                cnt += dp(i + 1, j + 1)
            
            memo[(i, j)] = cnt
            return memo[(i, j)]
        
        return dp(0, 0)
