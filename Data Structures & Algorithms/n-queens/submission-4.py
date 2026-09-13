class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag = set() # row - col
        diag_n = set() # row + col
        ans = []

        # print(board)
        def backtrack(row: int):
            if row >= n:
                copy = ["".join(item) for item in board[:]]
                ans.append(copy)
                return
            
            for col in range(n):
                # try to place queen in row col based on sets
                if (
                    col not in cols and
                    row - col not in diag and
                    row + col not in diag_n
                ):
                    board[row][col] = "Q"
                    cols.add(col)
                    diag.add(row - col)
                    diag_n.add(row + col)

                    backtrack(row + 1)

                    board[row][col] = "."
                    cols.remove(col)
                    diag.remove(row - col)
                    diag_n.remove(row + col)
        
        backtrack(0)
        return ans