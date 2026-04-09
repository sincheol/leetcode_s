import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = defaultdict(int)

res = 0
left = 0

for i in range(len(arr)):
    cnt[arr[i]] += 1
    while True:
        n = min(cnt.keys())
        m = max(cnt.keys())
        if m - n <=2:
            break
        cnt[arr[left]]-=1
        if cnt[arr[left]]==0:
            del cnt[arr[left]]
        left+=1
        
    if i-left+1>res:
        res = i-left+1

print(res)
