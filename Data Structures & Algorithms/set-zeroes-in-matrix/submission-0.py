class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        ROW, COL = len(matrix), len(matrix[0])

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(ROW):
            for c in range(COL):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        
        return
        
        