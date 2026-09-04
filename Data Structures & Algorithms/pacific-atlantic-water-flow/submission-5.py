class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific_cells = set() # rows[0][col] + rows[row][0]
        # atlantic_cells = set() # rows[n -1][col] + rows[row][n - 1]
        pac = set()
        atl = set()

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])

        def valid(row: int, col:int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row: int, col: int, visited: set):
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                r, c = stack.pop()

                for dr, dc in moves:
                    nr, nc = dr + r, dc + c
                    if  (
                        valid(nr, nc) and 
                        not (nr, nc) in visited and
                        heights[r][c] <= heights[nr][nc]
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            
            return
        
        # dfs for rows
        for row in range(ROWS):
            dfs(row, 0, pac)
            dfs(row, COLS - 1, atl)
        
        for col in range(COLS):
            dfs(0, col, pac)
            dfs(ROWS - 1, col, atl)
        
        output = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    output.append((row, col))
        
        return output
        