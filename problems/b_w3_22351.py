import sys


'''
어디서 끊을까?

'''

def calc(input):
    l_in = len(input)
    l = list(map(int,[input[0],input[:2],input[:3]]))

    for i in l:
        tmp = i
        s = ""

        while len(s)<l_in:
            s += str(tmp)

            if s == input:
                return i, tmp
            
            tmp+=1


input = sys.stdin.readline().rstrip()
print(*calc(input))

