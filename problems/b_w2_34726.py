import sys

'''
트랙 한바퀴 T

T//2로 나눴을 때 몫이 홀수 -> 앞쪽
짝수 -> 뒤쪽




'''

N, T = map(int, sys.stdin.readline().rstrip().split())
car = list()
s = 0
for _ in range(N):
    d, i = sys.stdin.readline().rstrip().split()
    s+=int(i)
    car.append((s % T, d))

car.sort(key = lambda x: x[0])

res= list()

for i in range(1,N):
    if abs(car[i][0]-car[i-1][0])<=1000:
        res.append(car[i][1])



if car[N-1][0] >=T-1000:
    res.append(car[0][1])



if len(res)==0:
    print(-1)
else:
    res.sort()
    print(*res)  
