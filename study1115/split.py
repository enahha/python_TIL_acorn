
my = [ 'first.c', 'info.h', 'define.py', 'test.py' ]
# 문제 1, 확장명 분리
# 문제 2, 결과 'h'데이터만 출력 if~~

tem = ''
for i in my:
    tem = i.split('.')
    if tem[1] == 'h' or tem[1] == 'c':
        print(tem)