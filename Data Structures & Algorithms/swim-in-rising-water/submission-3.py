from collections import deque
from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap = [(grid[0][0], 0, 0)] # (time-so-far, r, c)
        visited = set()

        def valid(row: int, col: int) -> bool:
            return 0 <= row < N and 0 <= col < N

        visited.add((0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            
            if r == N -1 and c == N - 1:
                return t
            
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        


        