class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # only move into valid
        # modify in place
        # dfs into 4 nearby positions
        # run only on start of character
        ROWS, COLS = len(board), len(board[0])

        def valid(row: int, col: int) -> bool:
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row: int, col: int, i: int):
            if i == len(word):
                return True
            
            # check if we can step into this cell
            if not valid(row, col) or board[row][col] != word[i]:
                return False

            # else mark character as visited and do a dfs search 
            char = board[row][col]
            board[row][col] = '#'
            ans = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )
            board[row][col] = char
            return ans
        

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
        
        