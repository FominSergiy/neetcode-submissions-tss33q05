class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        
        rows_used = set()
        cols_used = set()
        diag_used = set() # row - col_idx
        anti_diag_used = set() # row + col_idx

        def backtrack(row_idx: int):
            if row_idx >= n:
                # print(board)
                ans.append(["".join(row) for row in board])
                return
            
            for col_idx in range(n):
                # valid space for queen we can occupy
                if (
                    row_idx not in rows_used and
                    col_idx not in cols_used and
                    (row_idx - col_idx) not in diag_used and
                    (row_idx + col_idx) not in anti_diag_used
                ):
                    rows_used.add(row_idx)
                    cols_used.add(col_idx)
                    diag_used.add(row_idx - col_idx)
                    anti_diag_used.add(row_idx + col_idx)
                    board[row_idx][col_idx] = 'Q'

                    backtrack(row_idx + 1)

                    rows_used.remove(row_idx)
                    cols_used.remove(col_idx)
                    diag_used.remove(row_idx - col_idx)
                    anti_diag_used.remove(row_idx + col_idx)
                    board[row_idx][col_idx] = '.'
        
        backtrack(0)
        # print(ans)
        return ans