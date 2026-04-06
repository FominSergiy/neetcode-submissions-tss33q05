from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == '.':
                    continue

                if (
                    val in cols[col]
                    or val in rows[row]
                    or val in squares[(row // 3, col // 3)]
                ):
                    return False

                cols[col].add(val)
                rows[row].add(val)
                squares[(row // 3, col // 3)].add(val)

        return True                
            

        