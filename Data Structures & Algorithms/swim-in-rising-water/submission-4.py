from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        heap = [(grid[0][0], 0, 0)] # time, r, c

        def valid(row: int, col: int) -> bool:
            return 0 <= row < N and 0 <= col < N

        while heap:
            # global smallest t
            t, r, c = heapq.heappop(heap)

            if r == N - 1 and c == N - 1:
                return t
            
            # go over moves, visit and update t
            for dr, dc in moves:
                nr, nc = dr + r, dc + c
                if valid(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # min heap, another smallest value might be there
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        


        