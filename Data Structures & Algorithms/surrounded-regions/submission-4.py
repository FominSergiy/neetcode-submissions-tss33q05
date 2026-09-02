from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O"

        def bfs(row: int, col: int) -> list:
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if valid(nr, nc):
                        board[nr][nc] = "T"
                        q.append((nr, nc))
            return
        
        ROWS, COLS = len(board), len(board[0])
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        boarder_adj = set()
        # build a set of boarder-adjacent cells
        for row in range(ROWS):
            if board[row][0] == "O":
                boarder_adj.add((row, 0))
            if board[row][COLS - 1] == "O":
                boarder_adj.add((row, COLS - 1))

        for col in range(COLS):
            if board[0][col] == "O":
                boarder_adj.add((0, col))
            if board[ROWS - 1][col] == "O":
                boarder_adj.add((ROWS - 1, col))
        
        # mark save areas adjacent to boarder cell
        # skip otherwise
        for r, c in boarder_adj:
            board[r][c] = "T"
            bfs(r,c)

        # swap back in-place safe to 0 and non safe to X - the captured ones
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return
