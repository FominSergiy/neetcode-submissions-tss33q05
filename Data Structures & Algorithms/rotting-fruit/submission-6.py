from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        total_fresh = 0
        minutes = 0

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1
        
        def bfs(q: List[int]):
            nonlocal total_fresh
            nonlocal minutes

            while q and total_fresh > 0:
                for _ in range(len(q)):
                    # forgot to process layer by layer & update in-place
                    r, c = queue.popleft()

                    for dr, dc in moves:
                        nr, nc = dr + r, dc + c
                        if valid(nr, nc):
                            grid[nr][nc] = 2
                            total_fresh -= 1
                            queue.append((nr, nc))
            #  only increment once all cells within the current range are processed
                minutes += 1

            return minutes
        
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    total_fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        # bfs from multiple starting points at once
        bfs(queue)
        return minutes if total_fresh == 0 else -1