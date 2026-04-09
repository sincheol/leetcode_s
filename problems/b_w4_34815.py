import sys
'''
N, K
1<= <=N
K개 뽑기
K개의 정수 합 == (K+1)*x 가 가능?

N K가 주어짐

1 / 3 / 6 / 10 / 15 / 21

1~k까지 먼저 더해보기

k(k+1)/2 -> K+1의 배수가 되도록 하기

k/2가 남음. k는 짝수일때 항상 가능

홀수일경우는 안된다...그럼?
K개를 선택하는 것...
N=k+1 일 때
모든 sum -> 1~k+1를 하나씩 빼보기
S - (K+1) / S - 1까지 있다고 생각

연속된 k+1개의 수가 있는것.
연속된 n개의 수가 있을 때 그 안의 수에는 n의 배수가 항상 존재하게 됨!


'''


N, K = map(int, sys.stdin.readline().rstrip().split())

if K%2 == 0:
    print("YES")
else:
    if N > K:
        print("YES")
    else:
        print("NO")
