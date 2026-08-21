class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # only move into valid
        # modify in place
        # dfs into 4 nearby positions
        # run only on start of character
        ROWS, COLS = len(board), len(board[0])

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def backtrack(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if (
                not valid(r, c) or
                board[r][c] != word[i]
            ):
                return False
            
            char = board[r][c]
            board[r][c] = '#'
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )
            board[r][c] = char
            return found

        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False
        
        