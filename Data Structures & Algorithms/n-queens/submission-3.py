class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag = set() # row - col
        diag_n = set() # row + col
        ans = []

        # pass row, iterate on column
        def backtrack(row: int):
            if row >= n:
                ans.append(["".join(row) for row in board[:]])
                return
            
            for col in range(n):
                if (
                    col not in cols and
                    row - col not in diag and
                    row + col not in diag_n
                ):
                    cols.add(col)
                    diag.add(row - col)
                    diag_n.add(row + col)
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    cols.remove(col)
                    diag.remove(row - col)
                    diag_n.remove(row + col)
                    board[row][col] = "."


        backtrack(0)
        return ans
