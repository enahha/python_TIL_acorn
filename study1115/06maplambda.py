list1 = [10,20,40,50]
print(list1)

list1 = [n*10 for n in list1]
print(list1)

list1 = [10,20,40,50]
list2 = map(lambda x: x*10 , list1) #<map object at 0x00000214C1FCAD70>
list2 = list(map(lambda x: x*10 , list1)) #정답
print(list2)
print()
a_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(a_list[0])  #10
print(a_list[1])  #20
print(a_list[-1]) #80
print(a_list[-2]) #70
print()
print(a_list[1:5]) #[20, 30, 40, 50]












print()
print()