import sys


'''
1000x + 100y + 10z + t = (10(x+z)+y+t)^2
(10x+10z+y+t)^2
'''

input = int(sys.stdin.readline().rstrip())

while input < 9999:
    input +=1
    s = input

    a = s // 1000
    s = s % 1000
    b = s // 100
    s = s % 100
    c = s // 10
    s = s % 10
    d = s

    if (1000*a+100*b+10*c+d) == (10*(a+c)+b+d)**2:
        print(input)
        break

if input == 9999:
    print(-1)