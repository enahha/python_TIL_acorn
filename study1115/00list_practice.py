
books = list()
books.append( {'제목':'파이썬', '가격':500, '출판사':'케이비', '재고':27} )
books.append( {'제목':'리엑트', '가격':700, '출판사':'엘지', '재고':23} )
books.append( {'제목':'자바', '가격':990, '출판사':'삼성', '재고':7} )

# for 반복문으로 출력
for i in books:
    print(i)
print('='*100)
#================================================================================

mysite = dict()
mysite['kakao'] = '카카오'
mysite['google'] = '구글'
mysite['naver'] = '네이버'
print(mysite)

for key in mysite:
    print(key)          # key 값
    print(mysite[key])  # value값

print('-'*100)

for k,v in mysite.items():
    print(k)    # key 값
    print(v)    # value 값

print('-'*100)

for k in mysite.items():
    print(k)    # 튜플타입으로 출력 ()

# 딕트에 키보드 입력 등록, 기존내용수정, 기존내용삭제, 딕트 전체 출력, 한건조회
# 리스트에 추가, 삭제, 쪼개기[시작:끝-1]
