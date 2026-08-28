from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS solution moving outward and processings as queue

        queue = deque([])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        INF = 2147483647

        def valid(row: int, col: int) -> bool:
            return (
                0 <= row < ROWS and 
                0 <= col < COLS and 
                grid[row][col] == INF
            )
        
        def bfs(q: list):
            step = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = step

                    for dr, dc in moves:
                        new_r, new_c = r + dr, c + dc
                        if valid(new_r, new_c) and not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            q.append((new_r, new_c))
                step += 1
                            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited[r][c] = True
                    queue.append((r, c))
        
        bfs(queue)
        return
