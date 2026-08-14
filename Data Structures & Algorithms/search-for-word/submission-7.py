class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        # seen = set()
        # seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(r: int, c: int, i: int):
            if i == n:
                return True

            if (
                not valid(r, c) or 
                # (r, c) in seen or
                board[r][c] != word[i]
            ):
                return False
            
            # seen.add((r, c))
            char = board[r][c]
            board[r][c] = "#"
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            # seen.remove((r, c))
            board[r][c] = char
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    # backtrack here
                    if dfs(row, col, 0):
                        return True
        return False

        
        