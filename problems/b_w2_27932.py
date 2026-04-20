'''
점수차이 H
키차이가 H가능

N 사람 k 최소의 지친 사람수 최대값

키차이가 핵심

그럼 우선 차이 값을 다 구한다음에 (n)
+sort(nlogn)
+최대 인원수가 될 때까지 idx 증가(최대 n)

다만 추가할 때 둘다 추가해야함 근데 가운데 껴있으면? max값으로 넣어주기

2n+ nlogn
nlogn

'''


N, k, *arr = map(int,open(0).read().split())
if N<=k or N == 1:
    print(0)
    exit()

diff = list()

for i in range(N):
    if i == 0:
        diff.append(abs(arr[i]-arr[i+1]))
    elif i == N-1:
        diff.append(abs(arr[i]-arr[i-1]))
    else:
        diff.append(max(abs(arr[i]-arr[i-1]), abs(arr[i]-arr[i+1])))

diff.sort()

res = N-k-1



print(diff[res])


