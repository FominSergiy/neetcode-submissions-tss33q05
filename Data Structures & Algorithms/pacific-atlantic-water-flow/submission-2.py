class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific_cells = set() # rows[0][col] + rows[row][0]
        # atlantic_cells = set() # rows[n -1][col] + rows[row][n - 1]
        pac = set()
        atl = set()

        ROWS, COLS = len(heights), len(heights[0])

        def valid(row: int, col:int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        
        def dfs(row: int, col: int, visit: set, prev_height: int) -> bool:
            if (
                not valid(row, col)
                or (row, col) in visit or
                heights[row][col] < prev_height
            ):
                return
            
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res