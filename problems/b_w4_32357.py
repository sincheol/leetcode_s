import sys
'''
짝수일 때 4
2


홀수일 때 3
1


'''
tc = int(sys.stdin.readline().rstrip())
res = list()

for i in range(tc):
    s = sys.stdin.readline().rstrip()
    res.append(s)
    st = 0
    e = len(s)-1
    while st<e:
        if s[st]!=s[e]:
            res.pop()
            break
        st+=1
        e-=1
    
res = len(res)

print(res*(res-1))
