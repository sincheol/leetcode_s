import sys


res = 0
N, M = map(int, sys.stdin.readline().rstrip().split())
j = [0]

# init
for i in range(N):
    j.append(0)


for i in range(M):
    w, _ = map(int, sys.stdin.readline().strip().split())
    j[w] += 1

j.sort()

i=1
while i<N:
    if j[i]>=j[i+1]:
        res+=(j[i]-j[i+1]+1)
        j[i+1] +=(j[i]-j[i+1]+1)
    i += 1
print(res)

'''
최소를 다 빼버리고 있는애만 생각해도 됨.
다음번애가 같으면 +1 작으면 작은+1
크면 상관없음
'''