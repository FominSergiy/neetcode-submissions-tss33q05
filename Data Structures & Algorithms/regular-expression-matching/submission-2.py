class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            match = (
                i < len(s) and 
                (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":
                # 2 choices of skip or use if match
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]
            
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            return False
        
        return dfs(0, 0)
                
                
        