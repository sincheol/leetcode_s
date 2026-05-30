

N,Q, *q_arr = map(int,open(0).read().split())
arr = [[0 for _ in range(N)] for _ in range(3)]
midx1 = 0
midx2 = 0

def calc(a,b):
    if a==1:
        for i in range(0, 2):
            if b==1:
                for j in range(0,2):
                    arr[i][j] +=1

            elif b==N:
                for j in range(N-2, N):
                    arr[i][j] +=1

            else:
                for j in range(b-2, b+1):
                    arr[i][j] += 1

    elif a==4:
        for i in range(2, 4):
            if b==1:
                for j in range(0,2):
                    arr[i][j] +=1

            elif b==N:
                for j in range(N-2, N):
                    arr[i][j] +=1

            else:
                for j in range(b-2, b+1):
                    arr[i][j] +=1

    else:
        for i in range(a-2,a+1):
            if b==1:
                for j in range(0,2):
                    arr[i][j] +=1

            elif b==N:
                for j in range(N-2, N):
                    arr[i][j] +=1

            else:
                for j in range(b-2, b+1):
                    arr[i][j] +=1

idx = 1
for query in range(Q):
    idx+=1
    if q_arr[idx] == 1:
        idx+=1
        calc(q_arr[idx],q_arr[idx+1])
        idx+=1
    else:
        idx+=1
        print(max(arr[q_arr[idx]-1]))

