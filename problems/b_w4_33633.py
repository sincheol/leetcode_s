import sys

'''
Ai+1 = Ai /2 짝수
Ai+1 = 3Ai+1 홀수

An = 1 / 1<=i<N / Ai != 1

우선 2^(n-1) 이 최대의 수가 됨.

거기서부터 줄어들면서 -1을 했을 때 3으로 나눠지고 몫이 홀수가 되는가를 확인하고


'''

N = int(sys.stdin.readline().rstrip())

st = 1

res = []

def dfs(cur_val, depth):
    if depth == N:
        res.append(cur_val)
        return

    dfs(cur_val*2, depth+1)

    prev_val = (cur_val-1)
    if prev_val%3==0 and (prev_val//3)%2 == 1 and prev_val//3>1:
        dfs(prev_val//3, depth+1)

    
dfs(1,1)

res.sort()

print(len(res))
for i in res:
    print(i)
