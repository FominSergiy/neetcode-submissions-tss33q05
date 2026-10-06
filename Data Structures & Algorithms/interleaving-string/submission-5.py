class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # memo = {}
        # # think about this problem from perspective of s3
        # # at each point we pick from either and once we get to the end - base we return
        # def dp(i: int, j: int, k: int) -> int:
        #     if k == len(s3):
        #         return i == len(s1) and j == len(s2)
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     can = False
        #     if i < len(s1) and s1[i] == s3[k]:
        #         can |= dp(i + 1, j, k + 1)
            
        #     if j < len(s2) and s2[j] == s3[k]:
        #         can |= dp(i, j + 1, k + 1)
            
        #     memo[(i, j)] = can
        #     return memo[(i, j)]
        
        # return dp(0,0,0)

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        
        return dp[0][0]

