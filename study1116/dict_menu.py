import time
import sys  #System.exit(1)역할  sys.exit()프로그램 종료

def menuInsert():
    pass

def menuPrintAll():
    pass

def menuEdit():
    pass

def menuDelete():
    pass

def menuSearch():
    pass

def menuExit():
    pass


menu = {}
while True:
    print()
    sel = int(input('1.등록  2.출력  3.수정  4.삭제  5.검색  9.종료>>> '))
    if sel==9:
        print('딕트crud프로그램을 종료합니다\n')
        sys.exit()

    if sel==1:
        name = input('메뉴이름입력>>> ')
        price = int(input('가격입력>>> '))
        menu[name] = price
        print(name , '딕트등록이 성공했습니다')
    elif sel==2:
        print('--------------- 전체데이터 출력 --------------- ')
        for i,(j,data) in enumerate(menu.items()):
            print(i,j,data)
    elif sel==3:
        name=input('수정 대상메뉴입력>>> ')
        if menu.get(name) == None:
            print(name, '수정대상의 데이터가 없습니다')
        else:
            edit=int(input(name + '키값의 value입력>>> '))
            menu[name] = edit
            print(name, '대상 데이터 수정 성공했습니다')
    elif sel==4:
        #remove(),del 딕트[],pop()/pop(값)사용해서 해당항목 삭제처리 3시에 다시 실습 
        name=input('삭제대상 메뉴입력>>> ') 
        if menu.get(name)==None: 
            print(name, '삭제대상 데이터가 없습니다')
        else:
            menu.pop(name)  
            print(name, '데이터가 삭제 되었습니다')
            print()
            time.sleep(0.5)
            for k,v in menu.items():
                print(k, ':', v)  
    elif sel==5:
        #한건 key매칭으로 출력, 이미전체출력은 sel==2구문에서 처리 
        find=input('조회key 입력>>>')
        if menu.get(find) == None:
            print(find + '조회 대상 데이터가 없습니다')
        else:
            print(find , ':' , menu[find] , ' 조회성공입니다')
    else:
        print('숫자번호를 정확히 입력하세요')
