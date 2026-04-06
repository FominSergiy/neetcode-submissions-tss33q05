class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # valid rows
        for row in range(n):
            row_unique = set()
            print(board[row])
            for col in range(n):
                num = board[row][col]
                if num in row_unique:
                    return False
                
                if num != '.':
                    row_unique.add(num)
        
        # valid cols
        for col in range(n):
            col_unique = set()
            for row in range(n):
                num = board[row][col]
                if num in col_unique:
                    return False

                if num != '.':
                    col_unique.add(num)
        
        # valid sub sqrs
        for row_iter in range(0,9,3):
            for col_iter in range(0,9,3):
                unique = set()
                # print(f"{row_iter}-{col_iter}")
                for row in range(row_iter, row_iter + 3):
                    for col in range(col_iter, col_iter + 3):
                        num = board[row][col]
                        if num in unique:
                            return False

                        if num != '.':
                            unique.add(num)
        
        return True
                
            

        