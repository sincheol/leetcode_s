import sys

'''
주어진 주문서 전부 소모
행운 0
0+n
0*m
'''


l = sys.stdin.readline().rstrip().split()
n = int(l[0])
m = int(l[1])

s = 0
l = sys.stdin.readline().rstrip().split()
for i in range(n):
    s+=int(l[i])

l = sys.stdin.readline().rstrip().split()
for i in range(m):
    if int(l[i])==0:
        continue
    s*=int(l[i])

print(s)