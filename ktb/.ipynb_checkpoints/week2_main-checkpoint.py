'''

TODO : 첫 작성 때 메모장이 비었다는 print문이 나옴 손봐야함...
삭제시에 비밀번호를 두번 입력해야함... 기능을 추가하면서 작성하다보니 함수들 기능이 너무 재활용하기 힘들어졌음..
iterator, generator는 메모리에 한번에 올리지않고 필요한만큼 꺼내서 쓸 수 있다. 즉 메모리를 효율적으로 사용가능
여기서는 메모장의 용량이 너무 커져 json을 읽어와 list에 저장할 때 문제가 될 수 있는 것에 적용가능

1-5. 비동기 처리 – asyncio를 사용해 병렬 처리 적용

-----------------------------------------------------------------------
해결
decrypt되고 나서 문자열이 제대로 출력되기는 하는데 \n이 작동을 안해서 줄바꿈이 적용 안됨 -> split의 return은 list type(join으로 해결)
비밀번호는 16 24 32 byte만 지원... 해당되는 숫자가 아니면 err로 해결
========================================================================
예상가능한 err
각 기능별로 접근
*작성
    ***title과 content에 공백을 작성하면 나지 않을까*** 
    => 없는 번호라고 error.. read_f의 로직이 title과 content가 빈칸이면 벗어난 index를 사용자가 입력했다고 판단하게 되어있어서..
*조회 수정 삭제
    메모장이 생성되지 않았는데 조회하려 함
    idx에 해당되지 않는 숫자 작성 -> 숫자가 아닐수도 있겠다
*******사용자가 메모장이름을 "(잠금) "으로 시작하는 형태로 작성하면 메모장은 영원히 잠김...ㅋㅋㅋㅋㅋㅋ -> json파일을 하나 더 생성해서 잠김파일을 관리하면 해결됨*******
'''
import asyncio
import week2_utils

async def main():
    c = '작성'
    r = '조회'
    u = '수정'
    d = '삭제'
    a = '추가기능'
    e = '종료'
    while(True):
        try:
            i = int(input(f'메뉴를 선택해주세요 : (1.{c} 2.{r} 3.{u} 4.{d} 5.{a} 6.{e})'))
            if i == 1:
                #작성
                await week2_utils.create_f(i,"","")
            elif i == 2:
                #조회
                print(r)
                try:
                    title,content = await week2_utils.read_f(r)
                    print(f'Title : {title}\n{content}')#내용 출력
                except Exception as error:
                    print(error)
                    continue
            
            elif i == 3:
                #수정
                '''
                수정, 삭제의 경우 파일을 한줄씩 읽으면서 tmp파일에 복사함
                이때 수정(삭제)되는 파일의 title이면 tmp에 작성하지 않음
                os.replace method를 이용해 parsing이 끝나면 원본파일 삭제 후 tmp를 원본 파일이름으로 변경(atomic operation(하나 실패시 모두 실패)임)
                '''
                print(u)
                try:
                    title, content = await week2_utils.read_f(u) #읽어올 번호 입력받아 title content return
                except Exception as error:
                    print(error)
                    continue
                content = week2_utils.write_c() #새로 입력받기
                await week2_utils.create_f(i, title, content)
            
            elif i == 4:
                #삭제
                print(d)
                try:
                    title, content = await week2_utils.read_f(d)
                except Exception as error:
                    print(error)
                    continue
                await week2_utils.create_f(i,title, content)
                print('삭제 완료')
            elif i == 5: #없음...
                print(a)
            elif i == 6: #종료
                print(e)
                break
        except Exception as error:
            print('1~6으로 골라주세요')
        

asyncio.run(main())