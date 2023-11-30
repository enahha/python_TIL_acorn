# 셋{} 추가, 삭제가능 add(), discard(), remove()
m = {200, 500, 300, 600, 100, 200, 200, 300, 900}
print(m)    # 중복을 제거하고 순서와 관계없이 출력됨

m.add(111)
print(m)

m.discard(250)      # 값이 없어도 에러가 없음, 데이터가 없으면 실행 중 무시하고 처리
print(m)
m.discard(111)     # 있으면 지워줌
print(m)

try:
    m.remove(250)       # 데이터가 없으면 실행중 에러 발생
    print(m)
except:
    pass

# remove() 메소드는 지우려는 엘리먼트가 존잰하지 않으면 KeyError가 발생하지만 discard() 메소드는 엘리먼트가 없어도 정상종료한다

m.add('ㅣㄴ')
print(m)