import sys

'''
좋은쌍찾기
약수의 개수가 정확히 2개?
n+1이 소수인가 를 구하기
'''

def isprime():
    max_val = 10001
    arr = [True] * (max_val)
    arr[0] = arr[1] = False
    for i in range(2,int(max_val**0.5) + 1):
        if arr[i]:
            for j in range(i**2, max_val, i):
                arr[j] = False

    tc = int(sys.stdin.readline().rstrip())
    N = list()
    for i in range(tc):
        N.append(int(sys.stdin.readline().rstrip())+1)

    for i in N:
        if arr[i]:
            print(1)
            print(f"1 {i}")
        else:
            print(0)


if __name__ == "__main__":
    isprime()
    