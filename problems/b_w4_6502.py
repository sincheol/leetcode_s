import sys
'''
w//2
l//2
'''



cnt = 0
res = list()
while True:
    cnt+=1
    input = list(map(int,sys.stdin.readline().rstrip().split()))
    if len(input) == 1:
        break
    if input[0]**2>=((input[1]/2)**2+(input[2]/2)**2):
        res.append(f"Pizza {cnt} fits on the table.")
    else:
        res.append(f"Pizza {cnt} does not fit on the table.")


for i in range(cnt-1):
    print(res[i])