'''
그 전 값을 최소 가정 / 지금 3가지 중 선택 했을 때 업데이트하고 마지막에 min
'''

N, *arr = map(int,open(0).read().split())



r = arr[0]
g = arr[1]
b = arr[2]

for i in range(3,N*3,3):
    t_r,t_g,t_b = r,g,b
    c_r,c_g,c_b = arr[i:i+3]

    t_r = min(g,b) + c_r
    t_g = min(r,b) + c_g
    t_b = min(r,g) + c_b

    r,g,b = t_r, t_g, t_b


print(min(r,g,b))

