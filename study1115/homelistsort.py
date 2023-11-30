#homelistsort.py
data = [4,7,9,1,2] 
#알고리즘 준비운동 시작 별출력
#알고리즘 시작 소트 (선택소트, 버블소트, 삽입소트)
#for 중첩 반복문 해결

#1회 [1, 7, 5, 4, 2]
#2회 [1, 2, 7, 5, 4]
#3회 [1, 2, 4, 7, 5]
#4회 [1, 2, 4, 5, 7]


temp = 0
for x in range(len(data)-1):
    for y in range(x, 5):
        if data[x] > data[y]:
            # temp = data[x]
            # data[x] = data[y]
            # data[y] = temp
            data[x], data[y] = data[y], data[x]
    print(data)
print('최종 : ' , data)


print()
print('-' * 100)