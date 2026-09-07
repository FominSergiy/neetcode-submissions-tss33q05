from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)] # (time so far, row, col)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def valid(row: int, col: int) -> bool:
            return 0 <= row < N and 0 <= col < N

        # again, heap lets us pick the smallest candidate next
        # so even if we go over neighbors, next node with lowest functions t will be
        # picked.
        # doing that over and over again, we consistently pick node with smallest t
        # therefore, we reach the end with optional t
        while heap:
            t, r, c = heapq.heappop(heap)
            # global smallest t

            # exit if we reached cell at n - 1, n - 1
            if r == N - 1 and c == N - 1:
                return t
            
            # otherwise go over neighbors
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # min heap, another smallest value might be there
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return 0


        