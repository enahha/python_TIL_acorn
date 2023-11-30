#09lambda.py

def add(x,y):
    hap = x+y
    return hap

print('일반식 결과 =', add(12,7)) 
print('람다식 결과 =', (lambda x,y: x+y)(12,7))

data = lambda a,b : a+b
print('람다식 결과 =', data(12,7))
