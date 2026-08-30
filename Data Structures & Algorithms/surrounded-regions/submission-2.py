from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O"

        def bfs(row: int, col: int) -> list:
            queue = deque([(row, col)])
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        # check if cell is in boarder
                        if valid(nr, nc):
                            board[nr][nc] = "T"
                            queue.append((nr, nc))
            return
        
        ROWS, COLS = len(board), len(board[0])
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        
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
                    
        for row, col in boarder_cells:
            board[row][col] = "T"
            bfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
        return