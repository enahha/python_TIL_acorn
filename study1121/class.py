'''
class Emp:
    전역변수 및 생성자 및 함수기술
    title = '화요일'
    def __init__(self, title):
        self.title = title

    def insert(self):
        print('insert 제목 ', self.title)

    def display(self):
        print

ob = new Emp('hong')
ob.insert   # insert 제목 hong
'''

'''
--파이썬에서 클래스 상속
class HBEmp(Emp):
'''