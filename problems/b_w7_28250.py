import sys
from collections import defaultdict
'''
0<- 두개의 숫자가 1이상
1<- 둘다 0
2<- 0과 1

결국 0,1이 몇개인가
0끼리 or 0과 나머지 조합 -> 1
01의 조합 -> 2
이것들을 통해서 합을 구함
'''
a = list(map(int, sys.stdin.read().rstrip().split()))
d = defaultdict(int)

for i in range(1,a[0]+1):
    if a[i] == 0:
        d[0] += 1
    elif a[i] == 1:
        d[1] +=1

o = (d[0]*(d[0]-1))//2 + (d[0]*(len(a[1:])-d[1]-d[0]))
t = (d[0]*d[1])

print(o+(2*t))