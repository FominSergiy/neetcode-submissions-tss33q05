class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # again, use 2 pointers i j and advance i only when match to j
        # 2 choises - advance or not
        memo = {}

        def dp(i: int, j: int) -> int:
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            cnt = dp(i + 1, j)
            if s[i] == t[j]:
                cnt += dp(i + 1, j + 1)
            
            memo[(i, j)] = cnt
            return memo[(i, j)]
        
        return dp(0, 0)