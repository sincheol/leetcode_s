import sys

tc = int(sys.stdin.readline().rstrip())

res = list()
for i in range(tc):
    h,w,n = map(int, sys.stdin.readline().rstrip().split())

    if n%h==0:
        t1 = n//h
        t2 = h
    else:
        t1 = (n//h)+1
        t2 = n%h
    res.append(100*t2+t1)


for i in range(tc):
    print(res[i])
