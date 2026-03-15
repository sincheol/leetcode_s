import sys

Q = int(sys.stdin.readline().rstrip())
cnt = list()

for i in range(Q):
    s = sys.stdin.readline().rstrip()
    cnt.append(0)
    for j in range(len(s)-2):
        if s[j:j+3] == "WOW":
            cnt[i]+=1
        j = j+2
    

for i in cnt:
    print(i)
    


