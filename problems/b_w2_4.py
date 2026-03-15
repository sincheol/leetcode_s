'''
a,b,c,d
drs -> 0< <=1000
60000

a - b(30000) - c(1000) - d(59000)

no drs = -1

기준 - 1000/ 확인 
res에 넣어 / 그중 가장 먼 곳에 있는애가 다시 기준 - 1000/확인


'''
import sys

input = sys.stdin.readline().rstrip()
n,t = map(int, input.split())

total = 0
arr = list()
d = dict()
for i in range(n):
    input = sys.stdin.readline().rstrip().split()
    total -= int(input[1])
    tmp = (total % t)
    arr.append(tmp)
    if not d[input[0]]:
        d[input[0]] = input[1]
    
    
    
arr = sorted(arr)

res = list()
for i in range(n):
    if i!=n-1:
        print(arr[i+1][0] - arr[i][0])
        if 0<arr[i+1][0] - arr[i][0] <=1000:
            print(arr[i][1])

            res.append(arr[i][1])
    else:
        if 0<arr[0][0]+t-arr[i][0]<=1000:
            res.append(arr[i][1])

if res == list():
    print(-1)
else:
    print(sorted(res))


