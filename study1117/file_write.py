import time
# f = open(1파일명,2모드w/r,3인코딩)
# with open(1파일명, 2'w', 3encoding='utf-8') as my:


# f = open(파일명,'wt/a',encoding='utf-8')
path  = '../data/test.txt'
f = open(path,'w',encoding='utf-8')
f.write('이순신\n')
f.write('lattee\n')
f.write('11-17-금\n')
f.write('3.14\n')
f.close()
time.sleep(0.3)
print(path, '파일저장 성공했습니다')

name  = '../data/sample.txt'
with open(name, 'w', encoding='utf-8') as my:
    my.write('카카오톡\n')
    my.write('카카오맵\n')
    my.write('카뱅크\n')
    my.write('1200\n')
    my.close()
time.sleep(0.3)
print(name, '파일저장 성공했습니다')    

# a는 이어쓰기
# w는 덮어쓰기
# x는 파일 생성 후 쓰기(만약 존재하는 파일이면 예러)
# r는 읽기