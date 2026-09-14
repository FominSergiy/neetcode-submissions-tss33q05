from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def valid(r, c) -> bool:
            return 0 <= r < N and 0 <= c < N
        
        # heap, traverse using the smallest value of t function
        # always pick the smallest, when reached end, that is the answer
        heap = [(grid[0][0], 0, 0)] # t, r, c
        while heap:
            t, r, c = heapq.heappop(heap)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(
                        heap, 
                        (
                            max(t, grid[nr][nc]),
                            nr, 
                            nc
                        )
                    )
        