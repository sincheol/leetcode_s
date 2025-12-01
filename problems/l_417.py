class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows = len(heights)
        cols = len(heights[0])
        res = list()
        visit1 = [[0] * cols for _ in range(rows)] #보다는 0 for _ in range(cols)사용을 권장.. 이러면 같은 list를 참조하게 되면서 예기치 못한 에러 발생할 수도
        #list comprehension은 새로운 list를 생성하기 때문에 독립적 : 안전
        visit2 = [[0] * cols for _ in range(rows)] #visit1먼저 방문하기 때문에 1에 방문된 상태면 공통으로 방문된 상태가 됨

        def dfs(i,j,v):
            if v[i][j]==1:
                return
            if visit1[i][j]==1:
                res.append([i,j])

            v[i][j] = 1
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                X = i+dx
                Y = j+dy
                if 0<=X<rows and 0<=Y<cols and v[X][Y]!=1 and heights[i][j]<=heights[X][Y]:
                    dfs(X,Y,v)
                    

        for i in range(rows):
            dfs(i,0,visit1)
        for i in range(cols):
            dfs(0,i,visit1)
        for i in range(rows):
            dfs(i,cols-1,visit2)
        for i in range(cols):
            dfs(rows-1,i,visit2)

        
        return res
'''
비는 자기 자신보다 높이가 같거나 낮은 쪽으로 이동가능
역으로 생각하면 각 모서리부분에서 움직일 수 있는 방향은 같거나 높은 방향
각 edge에서 갈 수 있는 node들의 교집합을 찾으면 되겠다.
len이 작은 곳의 ocean을 기준으로 찾으면 될 듯.
'''