color = ['yellow', 'red', 'orange', 'blue']

#  리스트 데이터 검색 in의 경우 검색이 성공이면 bool값으로 나옴

print(color)
while True:
    print()
    my = input('검색컬러입력   >>>>>>>>..')
    if my in color:
        print('결과', my in color)      # 결과가 bool값으로 나옴
        print(my+ '성공')               # 결과가 value로 나옴
    elif my == 'q' or my =='quit':
        print('프로글램 종료.')
        break