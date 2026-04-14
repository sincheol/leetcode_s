import sys

N = int(sys.stdin.readline())
arr = list()
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x : x[0])

before = 0
for i, j in arr:
    if before > i:
        i = before

    before = i+j

print(before)


