# map  : map() 함수를 사용하여 리스트의 요소 값을 바꿀 수 있다
## map(적용시킬_함수, 반복가능 객체, …)
def square(x):
    return x ** 2

a = [1, 2, 3, 4, 5, 6, 7]

square_a = list(map(square, a))
print(square_a)     #결과 [1, 4, 9, 16, 25, 36, 49]

## 람다식을 이용한 map
a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(square_a)     #결과 [1, 4, 9, 16, 25, 36, 49]

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(list(map(lambda x, y: (x*2, y*2), l1, l2)))       #결과 [(2, 10), (4, 12), (6, 14), (8, 16)]

# ==============================================================

# filter : 함수를 사용하여 리스트에서 특정 조건을 만족하는 요소만 뽑아 낼 수 있다.
## 음수값 추출
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
print('음수 리스트 :', minus_list)

## function을 지정해 주지 않더라도 iterable의 각 element 중 False인 것은 제외하고 반환한다.
l6 = [True, False, True, False]
print(list(filter(None, l6)))      #[True, True]

# ==============================================================

# reduce : 각 element를 왼쪽부터 오른쪽 방향으로 function을 적용하여 하나의 값으로 합친다.
## 예를들어 reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])라고 한다면, ((((1+2)+3)+4)+5)의 값을 반환
from functools import reduce
