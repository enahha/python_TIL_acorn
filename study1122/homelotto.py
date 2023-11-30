#해결1] import random 난수를 이용해 정수발생 1 ~ 45사이 6개숫자 
#해결2] 6개숫자 for,while 반복
#해결3] 난수중복발생하므로 중복체크 
#해결4] 원본출력, 소트해서 출력
#해결5] 6개숫자 리스트[] append(), 셋{} add() 

import random

lotto = set() 
result=True

while True:
    num=random.randint(1,45)
    if len(lotto) >= 6: 
        break
    else:
        lotto.add(num)

print()
print(lotto)

lotto2=list(lotto) 
lotto2.sort( )
print(lotto2)


print()
print('- ' * 50)