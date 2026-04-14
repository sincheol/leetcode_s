'''

i: 사용할 수 있는 동전
M: 만들어야하는 돈

만들어질 수 있는 경우의 수: 기존의 동전들로 만들 수 있는 경우의 수 + 지금 추가된 동전만큼 뺀 값을 만들 수 있었던 경우의 수
->지금 추가된 동전 하나만 추가하면 되니깐

M을 하나씩 증가시켜서 목표금액까지 올리면 됨

'''

i_arr = list(map(int,open(0).read().split()))
res = list()

idx = 1
for _ in range(i_arr[0]):
    N = i_arr[idx]
    idx+=1
    coins = [x for x in i_arr[idx:idx+N]]
    idx+=N
    M = i_arr[idx]
    idx+=1
    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i]+=dp[i-coin]

    res.append(dp[M])
    

for i in res:
    print(i)
    