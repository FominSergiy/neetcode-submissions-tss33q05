from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O"

        def bfs(row: int, col: int) -> list:
            region_to_skip = set()
            queue = deque([(row, col)])
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        # check if cell is in boarder
                        if valid(nr, nc) and not visited[nr][nc]:
                            region_to_skip.add((nr, nc))
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            return region_to_skip
        
        ROWS, COLS = len(board), len(board[0])
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False] * COLS for _ in range(ROWS)]
        
        boarder_cells = set()
        for row in range(ROWS):
            if board[row][0] == "O":
                boarder_cells.add((row, 0))
            if board[row][COLS - 1] == "O":
                boarder_cells.add((row, COLS - 1))
        
        for col in range(COLS):
            if board[0][col] == "O":
                boarder_cells.add((0, col))
            if board[ROWS - 1][col] == "O":
                boarder_cells.add((ROWS - 1, col))
        
        # exit early of no boarder cells
        if not boarder_cells:
            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] == "O":
                        board[row][col] = "X"
            return
                    
        extra_unreachable = set()
        for row, col in boarder_cells:
            visited[row][col] = True
            extra_unreachable = extra_unreachable.union(bfs(row, col))
        
        merged_set = extra_unreachable.union(boarder_cells)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in merged_set:
                    board[row][col] = "X"
        return