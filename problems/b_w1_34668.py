'''
국제선 -> 국내선 (4, 2)
국내선 -> 국제선 (4, 2)
막차 시간이 지났나? 안지났나?
50명
06 / 18 / 30 / 42 / 54
5타임
M명

06시

'''

input = list(map(int, open(0).read().split()))

marr = ['06', '18', '30', '42', '54']
for i in range(input[0]):
    b = input[i+1] // 50
    h = b//5
    m = (b%5)

    if h<=5:
        print(f'0{6+h}:{marr[m]}')
    else:
        print(f'{6+h}:{marr[m]}')