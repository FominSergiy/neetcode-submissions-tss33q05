class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        n = len(word)

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(r: int, c: int, i: int) -> bool:
            if i == n:
                return True
            
            # add condition for returning false
            if (
                not valid(r, c) or
                board[r][c] != word[i]
            ):
                return False
            
            char = board[r][c]
            board[r][c] = "#"
            # step into all 4 directions
            ans = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            board[r][c] = char
            return ans
            
          

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False

        
        