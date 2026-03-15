import sys


'''

N, M

빈칸, 벽, 바이러스, 백신, 탈출구

바이러스 : 상하좌우(활성화된 방향으로만 확산)
    한방향 / 모든 방향

백신하나당 바이러스 하나

백신이 있는 칸도 바이러스 확산됨. 바이러스 있으면 기존 하나 소모

탈출구도 바이러스 올 수 있음
.
#벽
UDLR한방향
A모든방향
V백신
SE 시, 탈

빈칸 제한 없음 /  모든방향, 백신 0개
벽 한개 이하 , 한방향 바이러스는 총 1개 이하
벽, 한방향 바이러스
백신 생김
모든방향 생김
'''

row, col = map(int, sys.stdin.readline().rstrip().split())

d = dict()
d['S'] = 0
d['E']= 0
d['O']= 0
d['V']= 0
d['A']= 0
d['#']= 0

res = 1

for i in range(row):
    s = sys.stdin.readline().rstrip()
    for j in s:
        if j == 'S':
            d['S']+=1
        if j == 'E':
            d['E']+=1

        if j == 'U':
            d['O']+=1
        if j == 'D':
            d['O']+=1
        if j == 'L':
            d['O']+=1
        if j == 'R':
            d['O']+=1

        if j == 'V':
            d['V']+=1
        if j == 'A':
            d['A']+=1
        if j == '#':
            d['#']+=1


if d['#']>1:
    res = 2
if d['O']>1:
    res = 2
if d['V']>0:
    res = 3
if d['A']>0:
    res = 4

if d['S'] != 1 or d['E'] != 1:
    res =-1
    
print(res)

