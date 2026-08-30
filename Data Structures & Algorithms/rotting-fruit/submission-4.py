from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        total_fresh = 0

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1
        
        def bfs(q: int):
            nonlocal minutes
            nonlocal total_fresh
    
            while total_fresh > 0 and q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if valid(nr, nc):
                            q.append((nr, nc))
                            total_fresh -= 1
                            grid[nr][nc] = 2
                minutes += 1
    
        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append([row, col])
                if grid[row][col] == 1:
                    total_fresh += 1
    
        bfs(queue)
        return minutes if total_fresh == 0 else -1
                    