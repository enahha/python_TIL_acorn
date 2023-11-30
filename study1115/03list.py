#03list.py
data = [47,79,65,13,29,34] 
print(data)
print()

print('갯수 =', len(data))
# print(), input(), int(), str(), type()
# float(), round(), len()
for i in  range(len(data)):
    print(data[i], end='\t')

# data = [47,79,65,13,29,34] 
# 리스트접근 리스트이름[위치]
# 리스트 시작첨자위치는 0번째 시작,  파이썬에서 문자열도 0번째시작 

print()
# list리스트 혼합데이터접근
product = ["엘쥐", '맥북', 250, 7.8, True, '맥북', 'B' ]
print(product)

product = ["엘쥐", ['맥북', 250, 7.8], True, '맥북', 'B', 35 ]
print(product)





print()
print('-' * 100)