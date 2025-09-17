import json
import os
from typing import Tuple
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
'''
함수 모음
'''

f_name = 'data.jsonl'
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


def read_memo()->None:
    '''
    read memo generator 한줄씩 읽음 한줄 -> {"title": title, "content": content} 형태
    '''
    if os.path.exists(f_name):
        with open (f_name, 'rb') as file:
            for line in file:
                yield json.loads(line)
    else:
        print('메모장이 비어있습니다.')

def read_f(a:str)->Tuple[str,str]:
    '''
    메모장 조회 title, content를 리턴해줌
    우선 read_memo generator method를 통해 사용자에게 title 목록 다 보여줌
    사용자에게 입력받아 해당 title, content 저장
    잠금이 되어있는 메모의 경우 decryption을 통해 content저장
    5회이상 틀리면 나가짐...다시 메뉴로 길이 틀리면 바로 메뉴로
    '''
    tmp = 0
    title = content = ""
    for memo in read_memo(): #generator기 때문에 매번 호출 해줘야 함... 
        tmp += 1
        print(f"{tmp} : {memo['title']}")
        
    if tmp==0:
        raise ValueError('메모가 비어있습니다.')


    n = int(input(f'{a}하고 싶은 메모(번호):')) #번호 선택 하겠지
    tmp = 0
    for memo in read_memo():
        tmp += 1
        if tmp == n:
            title = memo['title']
            content = memo['content']

    if title=="" and content=="":
        raise ValueError('없는 번호입니다.')

    if title.split(' ')[0]=='(잠금)': #잠금일때 비밀번호 확인
        tmp = 0
        while(True):
            if tmp>4:
                raise ValueError('5회 이상 틀림')
            tmp+=1
            pwd = input('비밀번호를 입력하세요')
            if len(pwd)!=(16 or 24 or 32):
                raise ValueError('잘못 입력하셨습니다.')
            try:
                content = decrypt(content, pwd)
            except Exception as error:
                print('잘못 입력하셨습니다.')
                continue
            if(content.split(' ')[0]=='rightpwd'):
                break
            else:
                print('잘못 입력하셨습니다.')
        content = "".join(content.split(' ')[1:])

    return title, content

def rew_memo(title:str)->None:
    '''
    해당 title의 메모를 삭제함
    '''
    try:
        with open('data.jsonl.tmp','w') as out_file:
            for memo in read_memo():
                if memo['title'] == title:
                    continue
                record = json.dumps(memo)
                out_file.write(record + '\n')
        os.replace('data.jsonl.tmp',f_name)
    except Exception as error:
        print(error)
def write_c()->str:
    '''
    사용자에게 content 입력을 받는 함수
    exit 입력시 종료 됨
    '''
    content = tmp = ''
    while(True):
        tmp = input(f'content : (종료 : exit)') #내용작성 어차피 제목 작성하면 내용도 작성되기 때문에 서로 idx가 같음 // 나중에 접근할 때 선택된 title의 idx활용하면 됨
        if tmp == 'exit':
            break
        content+=(tmp+'\n')
    return content

def create_f(i:int, title:str, content:str)->None:
    '''
    i==1
        사용자에게 title입력받고 write_c호출을 통해 content 입력받음
        ec_f를 통해 encryption여부와 함께 content를 encrypt
        file이 생성되어 있으면 a모드로 이어씀 / 없을 경우 w모드로 작성
    i==3,4
        title, content는 넘어옴
        rew_memo를 통해 해당 title의 메모를 삭제
    i==3
        잠금이었으면 title에 (잠금)은 지우고
        이후에는 encryption필요한지부터 1과 같음
    '''
    if i != 1: #우선 내용 삭제
        rew_memo(title)
    else: #1일때는 삭제 필요없음.. 내용 작성
        title = input(f'title :') #사용자에게 title입력받음
        content = write_c()
    if i!=4: #4일때는 메모쓰기 필요없음.. 메모뒤에 붙여넣기
        if title.split(' ')[0]=='(잠금)':
            title = "".join(title.split(' ')[1:])
        title ,content = ec_f(title, content)
        memo = {'title':title,'content':content} #for json style
        w_mode = '' #for writing mode.. write? append?
        if os.path.exists(f_name):
            w_mode = 'a'
        else:
            w_mode = 'w'
        with open(f_name, w_mode) as file:
            record = json.dumps(memo)
            file.write(record + '\n')
    print(f'{i} 완료')

def ec_f(title:str, content:str)->Tuple[str,str]:
    '''
    비밀번호 설정 여부 물어본 후 사용자에게 입력받음
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
