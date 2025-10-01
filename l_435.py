class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = sorted(intervals)
        l = len(intervals)
        cnt = 0
        before = -500001
        for s,e in i:
            if s<before:
                cnt+=1
                if e<before:
                    before = e
            else:
                before = e
        return cnt



'''
만약에 같은 idx시작이 있으면 처음껄 사용하면 됨.
어떤 범위안에 다른 범위가 들어오면 카운트가 시작돼야 함.
자기 자신 범위 안에 어떤 범위(시작과 끝)이 있으면 자기 자신은 없어져야함
'''