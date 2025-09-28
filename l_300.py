class Solution:
    def srch(self, res: List[int], n:int)->int:
        lidx = 0
        ridx = len(res)-1

        while lidx<ridx:
            midx = (ridx+lidx)//2
            if res[midx]==n:
                return midx
            elif res[midx]>n:
                ridx = midx
            else:
                lidx = midx+1
        print(lidx)
        return lidx
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = list()

        for n in nums:
            if not res or res[-1]<n:
                res.append(n)
            else:
                idx = self.srch(res, n)
                res[idx] = n

        return len(res)

'''
오른쪽에 자기 자신보다 큰게 몇개 있냐
오른쪽을 sorting해놓고 자기 자신보다 큰거 cnt
=========================================
O(n^2) -> 0->n-1 탐색, 그 전까지(0~i-1)의 개수+1과 비교해서 max
O(nlogn) -> 0->n-1탐색, 배열에서 본인보다 큰 애들중 가장 작은 애를 대체(bi srch)
'''