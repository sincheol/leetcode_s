class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        다 가능함
        다만 Loop가 생기는 순간 불가능해지는 문제
        만약에 dict안에 들어가있다면? impossible
        우선 numCourses안에 있는 건지 확인
        '''

        from collections import defaultdict
        l = [0 for _ in range(numCourses)]
        graph = defaultdict(list)


        for st, end in prerequisites:
            graph[st].append(end)

        def dfs(v):
            if l[v] ==1:
                return True
            if l[v] ==2:
                return False

            l[v] = 1

            for neighbor in graph[v]:
                if dfs(neighbor):
                    return True

            l[v] = 2
            return False




        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
