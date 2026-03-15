import sys

'''
서N,동M

mCn


'''
input = int(sys.stdin.readline().rstrip())

for tc in range(input):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    if n>(m//2):
        n = m-n


    a = 1
    b = 1
    tmp = n
    for i in range(n):
        a*=m
        m-=1
        b *= tmp
        tmp-=1


    print(a//b)