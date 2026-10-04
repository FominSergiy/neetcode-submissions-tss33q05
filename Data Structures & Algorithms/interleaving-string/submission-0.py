class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        def dp(i: int, j: int, k: int) -> bool:
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            can = False
            if i < len(s1) and s1[i] == s3[k]:
                if dp(i + 1, j, k + 1):
                    can = True

            if j < len(s2) and s2[j] == s3[k]:
                if dp(i, j + 1, k + 1):
                    can = True
            
            memo[i][j] = can
            return memo[i][j]

        
        return dp(0,0,0)