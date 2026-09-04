from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        total_fresh = 0

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1
        
        def bfs(q: list):
            minutes = 0
            nonlocal total_fresh

            while total_fresh > 0 and q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if valid(nr, nc):
                            grid[nr][nc] = 2
                            total_fresh -= 1
                            q.append((nr, nc))
                minutes += 1
            return minutes
        
        # build queue
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    total_fresh += 1
        
        ans = bfs(queue)
        return ans if total_fresh == 0 else -1