#02list.py

data = [4,7,5,1,2]  #첫번째 같은타입으로 구성
print(data)
print()

print('원본', end=' ')
for i in data:
    print(i, end=' ')
print()

data.sort()
print('소트', end=' ')
for i in data:
    print(i, end=' ')
print()

data.reverse()
print('역순' , end=' ')
for i in data:
    print(i, end=' ')
print()

print('합계 =', sum(data))





print()
print('-' * 100)