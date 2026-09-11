class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ansIdx, ansLen = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l, r = i, j
                if s[l] == s[r] and (
                    r - l <= 2 or
                    dp[l + 1][r - 1]
                ):
                    dp[l][r] = True
                    # only go if new value is larger, update
                    if ansLen < r - l + 1:
                        ansIdx = l
                        ansLen = r - l + 1
        
        return s[ansIdx: ansIdx + ansLen]
        