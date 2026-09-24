class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resIdx, resLen = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l, r = i, j
                if s[l] == s[r] and (
                    r - l <= 2 or
                    dp[l + 1][r - 1]
                ):
                    dp[l][r] = True
                    
                    if resLen < r - l + 1:
                        resLen = r - l + 1
                        resIdx = l
        
        return s[resIdx: resIdx + resLen]