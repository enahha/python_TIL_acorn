
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
print('원본 : ', n_list)

# 리스트 데이터에서 음수만 추출
## 람다식 이용해 추출
a = list(filter(lambda x: x<10, n_list))
print('람다식 리스트 사용 : ', a)

## list comprehension을 이용해 추출
b = [ x for x in n_list if x < 0 ]
print('리스트 축약식 사용 : ',b)