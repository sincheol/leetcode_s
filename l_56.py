class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = list()
        lidx = -1
        ridx = -1
        intervals.sort()
        for i in range(len(intervals)):
            if lidx == -1:
                lidx = intervals[i][0]
                ridx = intervals[i][1]
            else:
                if intervals[i][0]<=ridx:
                    if intervals[i][1]>ridx:
                        ridx = intervals[i][1]
                else:
                    res.append([lidx,ridx])
                    lidx = intervals[i][0]
                    ridx = intervals[i][1]
            if i == len(intervals)-1:
                res.append([lidx, ridx])

        
        return res


'''
lidx = -1(default)
lidx 가 default면 lidx를 지금으로 ridx도 지금으로
아니면
ridx보다 작은지 확인
작다면 ridx랑 비교해서 큰값을 ridx로
안작다면 lidx, ridx append
'''