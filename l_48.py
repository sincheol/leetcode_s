class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        
        for i in range(l//2):
            for j in range(i,l-i-1):
                sidx = [i,j]
                tmp = matrix[i][j]
                for _ in range(4):
                    store = matrix[sidx[1]][l-1-sidx[0]]
                    matrix[sidx[1]][l-1-sidx[0]] = tmp
                    tidx = sidx[0]
                    sidx[0] = sidx[1]
                    sidx[1] = l-1-tidx
                    tmp = store

                

        """
        Do not return anything, modify matrix in-place instead.
        """
        

'''
col num -> row num
n - row num -> col num
'''