# 04lambda.py
# mytest함수에서 x*3+2처리 
import time

def mytest(x):
    su = x*3+2
    return su

data = mytest(6)
print('일반식 결과 =', data)
print('람다식 결과 =', (lambda x: x*3+2)(6))
# lambda키워드  매개인자x :  수식

def myadd(a,b):
    hap = a+b
    return hap

print()
time.sleep(1)
value = myadd(12,7)
print('일반식 결과 =', value) # 12+7
print('람다식 결과 =', (lambda x,y: x+y)(12,7))







print()
print()