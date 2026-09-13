class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # for l and r pointer
        ans = 0
        # print(dp)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l, r = i, j
                # print(f"l: {l}, r: {r}")
                if s[l] == s[r] and (
                    r - l <= 2 or
                    dp[l + 1][r - 1]
                ):
                    dp[l][r] = True
                    ans += 1
        
        return ans