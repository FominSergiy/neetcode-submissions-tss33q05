class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1
        

        max_area = 0

        def dfs(r: int, c: int):
            stack = [(r, c)]
            area = 1
            grid[r][c] = -1 # modify in-place
            while stack:
                row, col = stack.pop()

                for dr, dc in moves:
                    nr, nc = row + dr, col + dc

                    if valid(nr, nc):
                        grid[nr][nc] = -1
                        stack.append((nr, nc))
                        area += 1
            
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area