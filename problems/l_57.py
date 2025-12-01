class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        res = list()

        while idx<len(intervals) and intervals[idx][1]<newInterval[0]:
            res.append(intervals[idx])
            idx+=1
        while idx<len(intervals) and intervals[idx][0]<=newInterval[1]:
            newInterval = ([min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])])
            idx+=1
        res.append(newInterval)
        res.extend(intervals[idx:])

    

        return res

'''
왼쪽에서 오른쪽으로 오름차순 ! / idx0->1순으로 탐색
겹치는거 시작점 ?idx0이 !의 idx 0, 1사이에 있으면 됨..
01사이에있으면 시작점은 !idx0 / 10사이면 ?idx0로 시작

끝점은 ?idx1이 똑같이 만족하면 끝
01사이에있으면 끝점은 !idx1 / 10사이면 ?idx1로 끝
idx 01모두 탐색해야됨

예외두개가 있네
겹치치도 않아서 끝에 그냥 insertion되는거
매번찾기는 아까우니깐 iter돌기전에 그냥 확인하고 돌리면 좀 더 빠를듯
너무 조건이 많아
===================================================
경우의 수 하나씩 없애기
ijij
ij
어차피 그냥 지나치는거는 newinterval[0]보다 interval[1]이 작을 경우에는 그냥 interval저장하면 됨
이제 사이에 끼는 것은 newinterval[1]이 interval[0]과 같거나 클때 사이에 껴있음
newinterval이 제일 클 수도 있음 여기까지 왔는데 insertion이 안일어났으면 지금 해야됨
이젠 남은거 그냥 다 넣어버려
'''