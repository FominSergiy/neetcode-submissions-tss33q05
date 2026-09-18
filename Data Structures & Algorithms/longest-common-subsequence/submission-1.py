class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # order has to matter within the same substr
        
        # TOP DOWN
        # memo = [[0] * len(text2) for _ in range(len(text1))]
        # # print(memo)
        # def dp(i: int, j: int) -> int:
        #     # we have reached the end
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if memo[i][j]:
        #         return memo[i][j]
            
        #     # advance both pointers on match
        #     if text1[i] == text2[j]:
        #         # return 1 + dp(i + 1, j + 1)
        #         memo[i][j] = 1 + dp(i + 1, j + 1)
        #         return memo[i][j]
            
        #     # otherwise, try to match by advancing either pointer by 1 and get the max
        #     # return max(dp(i + 1, j), dp(i, j + 1))
        #     memo[i][j] = max(dp(i + 1, j), dp(i, j + 1))
        #     return memo[i][j]
        
        # return dp(0, 0)

        # BOTTOM UP
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
            
