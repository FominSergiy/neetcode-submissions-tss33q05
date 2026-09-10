class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l, r = i, j
                if s[l] == s[r] and (
                    r - l <= 2 or
                    dp[l + 1][r - 1]
                ):
                    dp[l][r] = True
                    count += 1
        
        return count
        