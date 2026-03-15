import sys
from collections import defaultdict
'''

같은 수가 나오면 그 처음이 제일 긴 경우가 됨..
다음번은 그 다음 수로 시작하면 됨..
'''


n = int(sys.stdin.readline().rstrip())

l = list(map(int, sys.stdin.readline().rstrip().split()))

st, end = 0, 0
m = -1
#
cnt = defaultdict(int)

while end<n:
    # 앞에서부터 더하기
    cnt[l[end]] += 1

    #3개 이상이면 앞에서부터 계속 지우기
    while len(cnt.keys())>2:
        cnt[l[st]] -=1
        if cnt[l[st]] == 0:
            del cnt[l[st]]
        st+=1
    end+=1
    m = max(m,sum(cnt.values()))

print(m)