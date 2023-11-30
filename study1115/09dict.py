

# enumerate: 리스트의 원소에 순서값을 부여해주는 함수

mysite = {'naver':'네이버', 
          'google':'구글', 
          'kakao': '카카오'}

for i, j in enumerate(mysite):
    print(i, j, mysite[j])

print()
for i, j in enumerate(mysite, start=1): # 인덱스 첫 순서의 값을 지정
    print(i, j, mysite[j])

print()
for i,j in enumerate(mysite):
    print(j,mysite[j])

#+++++++++++++++++++++++++++++++++=
print()
for k,v in mysite.items():
    print(k, ':', v)