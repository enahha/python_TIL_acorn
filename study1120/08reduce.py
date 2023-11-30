# lambda, filter, map  임포트 지정안해도 사용가능
# reduce 임포트 강제지정

# 첫번째 import 파일명
# import LG

# 두번째 from 파일명 import 전역변수,함수이름 
# from LG  import user_id,user_pwd,terran,add,book

from functools  import reduce

print('20일 monday 저쩌구')
print('20일 monday 어쩌구')
print('람다식 08reduce.py')

su = list(range(1,11,1))
print(su) 
 
# 첫번째 일반함수 + reduce()
def myhap(x,y):
    total = x+y
    return total
print('일반식+reduce() 합계 =', reduce(myhap,su))

# 두번째 람다식 + reduce()
print('람다식+reduce() 합계 =', reduce(lambda x,y:x+y ,su))








print()
print('-' * 100)