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
        
        
        def dfs(row: int, col: int, visit: set) -> bool:
            # dfs into a valid square that is
            # greater than the current square and is valid
            stack = [(row, col)]
            visit.add((row, col))
            while stack:
                r, c = stack.pop()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (
                        valid(nr, nc) and 
                        heights[r][c] <= heights[nr][nc] and
                        (nr, nc) not in visit
                    ):
                        visit.add((nr, nc))
                        stack.append((nr, nc))

        # dfs into existing pac and atl cells only, build the set of such cells
        # through dfs
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
    
        # at the end the cell that exists in both of those sets is the answer
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res