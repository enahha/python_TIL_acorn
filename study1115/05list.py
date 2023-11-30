data=[3, 98, 7, 1, 6, 2]
print(data)

# 에러 data.remove(88)
data.remove(98) #데이터삭제
print(data)
data.pop()  # 마지막껏삭제 
print(data)
data.pop(2) # 2번째 삭제 
print(data)
del data[1]
print(data)
data=[]
print(data) # 전체삭제

# [3, 98, 7, 1, 6, 2]
# [3, 7, 1, 6, 2]
# [3, 7, 1, 6]
# [3, 7, 6]
# [3, 6]
# []


# list1 = list()             # 빈 리스트 생성하기 1
# list2 = []                 # 빈 리스트 생성하기 2
# list3 = list((1, 2, 3))    # 튜플데이터를 리스트화      

# 맨끝에 추가 append(), 중간위치삽입insert(위치,값)
# 삭제 pop() remove() del











print()
print()