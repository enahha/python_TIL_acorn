import time
# f = open(1파일명,2모드wt/a/r,3인코딩)
# with open(1파일명, 2'w', 3encoding='utf-8') as my:


# f = open(파일명,'wt/a/r',encoding='utf-8')
path  = './data/test.txt'
f = open(path,'r',encoding='utf-8')
data = f.read()

print(data)
print('-'  * 100)

f.close()
time.sleep(0.3)
print(path, '파일읽기 성공했습니다')


name  = './data/sample.txt'
with open(name, 'r', encoding='utf-8') as my:
    value = my.read()
    print(value)
   
time.sleep(0.2)
print(name, '파일읽기 성공했습니다')    




print()
print()