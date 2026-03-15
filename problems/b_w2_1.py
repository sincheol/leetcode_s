import sys

l = int(sys.stdin.readline().rstrip())
y = 0
k = 0
for i in range(l):
    s = sys.stdin.readline().rstrip()
    if s== "yonsei":
        y = i
    elif s=="korea":
        k = i

if y<k:
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")
``