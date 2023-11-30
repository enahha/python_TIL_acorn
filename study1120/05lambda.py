# 05lambda.py
# print('람다식 결과 =', (lambda x: x*3+2)(6))
# print('람다식 결과 =', (lambda x,y: x+y)(12,7))
# (lambda키워드  매개인자x :  수식)()

def mynote(a,b):
    if a%2==0:
        return a
    else:
        return b

print('일반식 결과 =', mynote(36,79))
# (lambda키워드  매개인자a,b : True if 조건하면 else False)(36,79)
print('람다식 결과 =' , (lambda a, b: a if a%2==0  else b)(36,79))










print()
print()