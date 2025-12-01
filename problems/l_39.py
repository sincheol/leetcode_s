class Solution:
    def __init__(self):
        self.res = list()
        self.c = list()
        self.t = 0
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.c = candidates
        self.t = target
        return self.calc(len(self.c)-1, 0, [])

    def calc(self, idx: int, total: int, l: list):
        if total == self.t:
            self.res.append(l[:])
            return

        if total>self.t or idx<0:
            return

        l.append(self.c[idx])
        self.calc(idx,self.c[idx]+total,l)
        l.pop()
        self.calc(idx-1,total,l)

        return self.res

    


'''
candidate에서 target값과 같거나 작은 수부터 시작해서
큰수부터 최대한으로 늘리고 작은 수까지 내려가면 될 듯
경우의수는 candidate과 해당 조합의 중복조합을 생각하면됨
중복 조합의 경우 cHr -> c+r-1Cr ----- r과 c-1중에 작은 수를 r에 넣으면 됨
//
지금 idx 자신을 제외하면 at least one은 다르니깐 그것도 생각해볼만
'''