class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        dfs?
        '''
        
        directions = [(-1,0), (1,0), (0,1),(0,-1)]
        row = len(board)
        col = len(board[0])
        visited = [[False]*col for _ in range(row)]

        def dfs(r,c,depth):
            if depth == len(word):
                return True
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                
                if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and board[nr][nc] == word[depth]:
                    visited[nr][nc] = True
                    if dfs(nr, nc, depth+1):
                        return True
                    visited[nr][nc] = False
            return False
                

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i,j, 1):
                        return True
                    visited[i][j] = False

        return False


    