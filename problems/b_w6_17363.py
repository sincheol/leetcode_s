import sys
'''
행을 열로
열은 뒤집어짐
'''
def tf(s):
    if s == '-':
        return "|"
    elif s == '|':
        return "-"
    elif s == '/':
        return "\\"
    elif s=='\\':
        return '/'
    elif s == '^':
        return "<"
    elif s== '<':
        return "v"
    elif s=='v':
        return ">"
    elif s=='>':
        return "^"
    else:
        return s


N, M = map(int, sys.stdin.readline().rstrip().split())

l = list()

res = [[0]* N for _ in range(M)]

for i in range(N):
    input = sys.stdin.readline().rstrip()
    for j in range(M):
        res[M-j-1][i] = tf(input[j])

for i in range(M):
    print(*res[i], sep = "")