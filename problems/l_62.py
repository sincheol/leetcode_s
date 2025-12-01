class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==2 and n==2:
            return 2
        tm = max(m-1,n-1)
        tn = min(m-1,n-1)
        if tn ==0:
            return 1
        res = tm+tn

        p = tm+1
        while p<tm+tn:
            res = res* p
            p+=1
        tmp = tn
        p = 2
        while p<tn:
            tmp*=p
            p+=1
        
        return res//tmp

'''
서로 다른 카드 2개에
같은 카드는 자리 바꾸는게 의미 없고 다른 카드끼리는 바꿔도 되고 그럼
전체조합 / 각 카드의 개수에서 나오는 조합
2 6
8 7
10 
3/2
m-1 / n-1

m+n-2~m+1
m * n 
'''

