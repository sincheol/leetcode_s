class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        lth = len(matrix)//2 if len(matrix)%2==0 else len(matrix)//2+1
        fcnt = len(matrix)*len(matrix[0])
        cnt = 0
        for r in range(lth):
            for i in range(r,len(matrix[0])-r): #1
                res.append(matrix[r][i])
                cnt+=1
            for j in range(r+1,len(matrix)-r): #2
                res.append(matrix[j][len(matrix[0])-r-1])
                cnt+=1
            if r!=len(matrix)-r-1:
                for k in range(len(matrix[0])-r-2,r-1,-1): #3
                    res.append(matrix[len(matrix)-r-1][k])
                    cnt+=1
            if r-1!=len(matrix[0])-r-2:
                for l in range(len(matrix)-r-2, r, -1):
                    res.append(matrix[l][r])
                    cnt+=1

            if cnt == fcnt:
                break

        return res

'''
0,0   ~.  0,c-1
r-1,0  ~.  r-1,c-1
1,1.  ~.  1,c-1-1

