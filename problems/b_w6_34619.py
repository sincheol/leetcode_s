import sys


'''
인원으로 나눠서 몇번째인지

나누고 몫 + (나머지있으면 +1)

소대수로 나눠서몇중대

나누고 몫 + (나머지 있으면 +1)



소대로 나눠
'''
a, b, n, k = map(int, sys.stdin.readline().rstrip().split())


i = k//n
l = k%n

if l!=0:
    i+=1

j = i//b
q = i%b

if q!=0:
    j+=1
else:
    q = b

print(j, q)