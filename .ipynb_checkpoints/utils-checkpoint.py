import json
import os
from typing import Tuple
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
'''
함수 모음
'''
d
def pad(text:str)->str:
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text:str)->str:
    return text[:-ord(text[-1])]

def encrypt(data:str, secretKey:str)->str:
    data = pad(data)
    secretKey = secretKey.encode('utf-8')
    cipher = AES.new(secretKey, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(data.encode('utf-8'))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return iv + ct

def decrypt(encryptedData:str, secretKey:str)->str:
    secretKey = secretKey.encode('utf-8')
    iv = encryptedData[:24]
    ct = encryptedData[24:]
    iv = b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(secretKey, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct).decode('utf-8'))
    return pt

def read_json()->list:
    f_name = 'data.json'
    memo = list()
    if os.path.exists(f_name):
        with open ('data.json', 'r') as file:
            memo = json.load(file)
    else:
        print('메모장이 비어있습니다.')
    return memo
def read_f(a:str)->Tuple[int,list,str,str]:
    tmp = 1
    memo = read_json()
    if len(memo)==0:
        print('메모징이 비어있습니다.')
        return 0, list(), "", ""
    for d in memo:
        print(f'{tmp} : {d["title"]} ') #제목과 번호 출력
        tmp+=1

    try:
        n = int(input(f'{a}하고 싶은 메모(번호):')) #번호 선택 하겠지
    except Exception as error:
        print(error)
        return 0,list(),"",""
    if n>len(memo) or n<1: #index범위 넘어가면 err
        print(f'1~{len(memo)} 사이로 골라주세요')
        return 0, list(), "", ""
    if memo[n-1]['title'].split(' ')[0]=='(잠금)':
        while(True):
            pwd = input('비밀번호를 입력하세요')
            if len(pwd)!=(16 or 24 or 32):
                print('잘못 입력하셨습니다.')
                return 0, list(), "", ""
            content = decrypt(memo[n-1]['content'], pwd)
            if(content.split(' ')[0]=='rightpwd'):
                break
            else:
                print('잘못 입력하셨습니다.')
                return 0, list(), "", ""
        content = content.split(' ')[1:]
        return n, memo, memo[n-1]['title'].split(' ')[1:], "".join(content) #선택한 idx가 필요하니 return 해줌
    return n, memo, memo[n-1]['title'], memo[n-1]['content'] #선택한 idx가 필요하니 return 해줌
def write_json(m:list)->None:
    with open ('data.json', 'w') as file:
        json.dump(m, file)
def write_c()->str:
    content = tmp = ''
    while(True):
        tmp = input(f'content : (종료 : exit)') #내용작성 어차피 제목 작성하면 내용도 작성되기 때문에 서로 idx가 같음 // 나중에 접근할 때 선택된 title의 idx활용하면 됨
        if tmp == 'exit':
            break
        content+=(tmp+'\n')
    return content

def create_f()->None:
    title = input(f'title :') #작성 - 우선 제목 먼저
    content = write_c()
    title, content = ec_f(title, content)
    memo = read_json()
    memo.append({'title':title, 'content':content})
    write_json(memo)
    print('작성 완료')

def ec_f(title:str, content:str)->Tuple[str,str]:
    '''
    비밀번호 설정 시 title앞에 (잠금)이라는 텍스트를 추가해서 구분
    비밀번호 설정 시 비밀번호는 사용자가 입력한 content에 "rightpwd "텍스트를 추가해서 같이 encrypt
    이렇게 하면 decrypt시에 맞는 비밀번호를 입력하면 rightpwd가 나올것이고 아니면 다른 글자가 나올거임.
    앞에 사용자가 설정한 pwd를 저장해도 되긴하는데
    그럼 사용자의 pwd들을 따로 관리해야해서 해당 프로젝트에서는 그냥 간단하게 관리자만 아는 정보 활용해서 encrypt decrypt를 함
    '''
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
    
    if ec == 'y': #비밀번호 설정이 되었으면 title앞에 (잠금)이 붙음
        title = '(잠금) ' + title
    return title, content
def pwd_val(memo:list,n:int)->int:
    while(True):
        pwd = input('정말 삭제하시려면 비밀번호를 입력하세요')
        if len(pwd)!=(16 or 24 or 32):
            print('잘못 입력하셨습니다.')
            return 0
        content = decrypt(memo[n-1]['content'], pwd)
        if(content.split(' ')[0]=='rightpwd'):
            return 1
        else:
            print('잘못 입력하셨습니다.')
            return 0