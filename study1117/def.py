
def book():
    title = '내 머리 돌려내'
    return title

def note():
    data = book()
    print(data)

note()

def mypage(name, x, y):
    print('name : ' , name)
    print('총점 : ', x+y)

mypage('정은아', 99, 80)