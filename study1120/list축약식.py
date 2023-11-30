# 문제 ,제곱 1~10숫자 구하기
for a in range(1,11) :
    su = a ** 2
    print(su, end=' ')

print()
for b in range(1,11):
    su = pow(b,2)
    print(su, end=' ')

# 축약식으로 구하기
print()
my_list = [ pow(c,2) for c in range(1,11) ]     #권장(순서대로 나옴)
print(my_list)

print()
my_set = { d**2 for d in range(1,11) }          # 비권장(순서가 섞여서 나옴)
print(my_set)

# lambda와 map으로
print()
a = [1, 2, 3, 4, 5, 6, 7]
a = list(map(lambda x : x ** 2 , a))
print(a)