class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cant use visited since I need to revisit

        # BOTTOM UP
        # ROWS, COLS = m, n
        # moves = [(1, 0), (0, 1)]

        # def valid(r: int, c: int) -> bool:
        #     return 0 <= r < ROWS and 0 <= c < COLS
        
        # memo = [[0] * COLS for _ in range(ROWS)]
        # def dfs(r: int, c: int) -> int:
        #     if r == ROWS - 1 and c == COLS - 1:
        #         return 1
            
        #     if memo[r][c]:
        #         return memo[r][c]
            
        #     ways = 0
        #     for dr, dc in moves:
        #         nr, nc = dr + r, dc + c
        #         if valid(nr, nc):
        #             ways += dfs(nr, nc)
            
        #     memo[r][c] = ways
        #     return memo[r][c]
        
        # ans = dfs(0, 0)
        # return ans

        # TOP_DOWN
        # each dp[i]
        ROWS, COLS = m, n
        # need this range to be + 1 since at 1st loop invocaton I am checking i + 1, j + 1
        # which is at COLS + 1, ROWS + 1
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS - 1] = 1 # final

        # build from end
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                dp[row][col] += dp[row + 1][col] + dp[row][col + 1]
        
        return dp[0][0]
