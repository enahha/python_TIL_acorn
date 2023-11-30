import math
import time
import random


x = 9
y = 5
ret1 = x % y #나머지
ret2 = x // y #몫을 정수값으로
ret3 = x == y
ret4 = x != y
ret5 = x ** y #거듭제곱

print(ret1, ret2, ret3, ret4, ret5)


#############################

print(math.sqrt(25))    #결과값을 실수로
print(math.sqrt(81))
print(math.pow(5,2))    # 25.0
print(5**2) #25
# 2진수 = bin()
# 4진수 = oct()
# 8진수 = hex()


##############################
# 실수형 random
print('실수 난수', random.random())
# 정수형 randint
print(random.randint(1,45)) #1-45까지 랜덤
