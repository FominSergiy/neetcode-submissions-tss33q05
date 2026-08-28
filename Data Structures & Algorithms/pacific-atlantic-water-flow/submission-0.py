class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_cells = set() # rows[0][col] + rows[row][0]
        atlantic_cells = set() # rows[n -1][col] + rows[row][n - 1]

        ROWS, COLS = len(heights), len(heights[0])

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        def valid(row: int, col:int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        for row in range(ROWS):
            for col in range(COLS):
                # add pacific
                if row == 0 or col == 0:
                    pacific_cells.add((row, col))

                if row == ROWS - 1 or col == COLS - 1:
                    atlantic_cells.add((row, col))
        
        def dfs(row: int, col: int) -> bool:
            reached_pacific = False
            reached_atlantic = False
            stack = [(row, col)]
            seen = set([(row, col)])
            while stack:                
                r, c = stack.pop()

                if (r,c) in pacific_cells:
                    reached_pacific = True
                    # continue
                
                if (r, c) in atlantic_cells:
                    reached_atlantic = True
                    # continue

                if reached_pacific and reached_atlantic:
                    return True

                # else explore
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (
                        (nr, nc) not in seen and 
                        valid(nr, nc) and
                        heights[r][c] >= heights[nr][nc]
                    ):  
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return False

        ans = []
        # print(pacific_cells)
        # print(atlantic_cells)
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col):
                    ans.append([row, col])
        return ans