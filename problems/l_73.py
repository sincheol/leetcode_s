class Solution:
    '''
    for rows
        for cols
            1,1부터 시작해서 row col 0인 부분에 저장
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = any(matrix[0][c] == 0 for c in range(cols))
        col_zero = any(matrix[r][0] == 0 for r in range(rows))
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,rows):
                for j in range(1,cols):
                    if matrix[i][0] == 0 or matrix[0][j]==0:
                        matrix[i][j] = 0
        
        

        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        