# 06lambda.py
# print('람다식 결과 =', (lambda x: x*3+2)(6))
# print('람다식 결과 =', (lambda x,y: x+y)(12,7))
# print('람다식 결과 =' , (lambda a, b: a if a%2==0  else b)(36,79))

a = list(range(1,11,1))
# print(a) 
# 람다식 단점 if~~elif~else사용불가 
# 람다식 단점 if~~ 에러
# 람다식 단점 if~~else 기본 
# 에러 print('람다식 결과 =' , (lambda a: a if a%2==0)(36)) 
# value = lambda a: a if a%2==0 else None
# print('람다식 결과 =' , value(36))
print('람다식 결과 =' , (lambda a: a if a%2==0 else None)(36))
print('람다식 결과 =' , list(map(lambda a: a%2==0,a)) )     # [False, True, False, True, False, True, False, True, False, True]
print('람다식 결과 =' , list(filter(lambda a: a%2==0,a)) )  # [2, 4, 6, 8, 10]



print('20일 월요일 저쩌구')
print('20일 월요일 어쩌구')





print()
print('-' * 100)