class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs approach where we check all 4 possible options making the base case
        # our validation checks
        ROWS, COLS = len(matrix), len(matrix[0])
        def valid(r: int, c: int) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS
        
        dp = {}
        def dfs(r: int, c: int, prev_val: int) -> int:
            if not valid(r, c) or matrix[r][c] <= prev_val:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            LIP = 1
            LIP = max(LIP, 1 + dfs(r + 1, c, matrix[r][c]))
            LIP = max(LIP, 1 + dfs(r - 1, c, matrix[r][c]))
            LIP = max(LIP, 1 + dfs(r, c + 1, matrix[r][c])) 
            LIP = max(LIP, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = LIP
            return dp[(r, c)]
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())


        