'''
TODO : 첫 작성 때 메모장이 비었다는 print문이 나옴 손봐야함...

-----------------------------------------------------------------------
해결
decrypt되고 나서 문자열이 제대로 출력되기는 하는데 \n이 작동을 안해서 줄바꿈이 적용 안됨 -> split의 return은 list type(join으로 해결)

========================================================================
예상가능한 err
각 기능별로 접근
*작성
    ***title과 content에 공백을 작성하면 나지 않을까*** 확인필요
*조회 수정 삭제
    메모장이 생성되지 않았는데 조회하려 함
    idx에 해당되지 않는 숫자 작성 -> 숫자가 아닐수도 있겠다

*비밀번호는 16 24 32 byte만 지원... 해당되는 숫자가 아니면 err로 해결

'''
import json
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode


def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt(data, secretKey):
    data = pad(data)
    secretKey = secretKey.encode('utf-8')
    cipher = AES.new(secretKey, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(data.encode('utf-8'))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return iv + ct

def decrypt(encryptedData, secretKey):
    secretKey = secretKey.encode('utf-8')
    iv = encryptedData[:24]
    ct = encryptedData[24:]
    iv = b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(secretKey, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct).decode('utf-8'))
    return pt

def read_json():
    f_name = 'data.json'
    memo = list()
    if os.path.exists(f_name):
        with open ('data.json', 'r') as file:
            memo = json.load(file)
    else:
        print('메모장이 비어있습니다.')
    return memo
def write_json(m):
    with open ('data.json', 'w') as file:
        json.dump(m, file)
def read_f(a):
    tmp = 1
    memo = read_json()
    if len(memo)==0:
        print('메모징이 비어있습니다.')
        return 0, 0, 0
    for d in memo:
        print(f'{tmp} : {d['title']} ') #제목과 번호 출력
        tmp+=1
        
    n = int(input(f'{a}하고 싶은 메모(번호):')) #번호 선택 하겠지
    if n>len(memo) or n<1: #index범위 넘어가면 err
        print(f'1~{len(memo)} 사이로 골라주세요')
        return 0, 0, 0
    if memo[n-1]['title'].split(' ')[0]=='(잠금)':
        while(True):
            pwd = input('비밀번호를 입력하세요')
            if len(pwd)!=(16 or 24 or 32):
                print('잘못 입력하셨습니다.')
                return 0, 0, 0
            content = decrypt(memo[n-1]['content'], pwd)
            if(content.split(' ')[0]=='rightpwd'):
                break
            else:
                print('잘못 입력하셨습니다.')
                return 0, 0, 0
        content = content.split(' ')[1:]
        return n, memo[n-1]['title'].split(' ')[1:], "".join(content) #선택한 idx가 필요하니 return 해줌
    return n, memo[n-1]['title'], memo[n-1]['content'] #선택한 idx가 필요하니 return 해줌

def write_c():
    content = tmp = ''
    while(True):
        tmp = input(f'content : (종료 : exit)') #내용작성 어차피 제목 작성하면 내용도 작성되기 때문에 서로 idx가 같음 // 나중에 접근할 때 선택된 title의 idx활용하면 됨
        if tmp == 'exit':
            break
        content+=(tmp+'\n')
    return content

def create_f():
    title = input(f'title :') #작성 - 우선 제목 먼저
    content = write_c()
    while(True):
        ec = input(f'비밀번호 설정 하시겠습니까?(y/n) (y)')
        if ec =='y':
            pwd = input('비밀번호를 작성해주세요(16, 24, 32글자)')
            if len(pwd)==(16 or 24 or 32): #비밀번호 설정가능 길이
                content = 'rightpwd '+content
                content = encrypt(content, pwd)
                break
            else: #비밀번호 길이 잘못됨 다시 설정할건지 물어보기
                print('길이를 16, 24, 32글자로 맞춰 주세요')
                continue
        else:
            break
    memo = read_json()
    if ec == 'y': #비밀번호 설정이 되었으면 title앞에 (잠금)이 붙음
        title = '(잠금) ' + title
    memo.append({'title':title, 'content':content})
    write_json(memo)
    print('작성 완료')

c = '작성'
r = '조회'
u = '수정'
d = '삭제'
a = '추가기능'
e = '종료'
while(True):
    i = int(input(f'메뉴를 선택해주세요 : 1.{c} 2.{r} 3.{u} 4.{d} 5.{a} 6.{e}'))
    if i == 1:
        create_f()
    elif i == 2:
        print(r)
        n,title,content = read_f(r)
        if n==0:
            continue
        print(f'Title : {title}\n{content}')#내용 출력
    elif i == 3:
        print(u)
        n, memo = read_f(u)
        if n==0:
            continue
        content = write_c()
        memo[n-1]['content'] = content
        write_json(memo)
    elif i == 4:
        print(d)
        n, memo = read_f(d)
        del memo[n-1]
        write_json(memo)
        print('삭제 완료')
    elif i == 5:
        print(a)
    elif i == 6:
        print(e)
        break