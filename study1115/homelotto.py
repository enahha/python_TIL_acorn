# 문제 1, 난수를 이용해 정수 발생 1~45
# 문제 2, 6개 숫자 for, while 반복
# 문제 3, 중복체크
# 문제 4, 원본출쳑, sort()해서 출력
# 문제 5, 6개숫자 리스트[] append(), 셋{} add() 
import random

# 리스트 길이 지정하기
num = list(0 for i in range(0,5))
print(num , '\n\n')

lotto = [2, 2, 2, 63, 63, 13]
# for a in range(6):
#     temNum = random.randint(1,45)
#     lotto.insert(a, temNum)
# set(lotto)
# lotto.sort()
for a in range(5):
    for b in range(a+1, len(lotto)):
        if lotto[a] == lotto[b]:
            del lotto[b]
            lotto.insert(b, random.randint(1,45))


print(lotto)
