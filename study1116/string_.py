
data = 'coffee latte pyhon easy'
print(data.split())  #['coffee', 'latte', 'pyhon', 'easy']
print(list(data))    #['c', 'o', 'f', ~~~' 'e', 'a', 's', 'y']

#==============================================================
# 문자열 찾기 : find(), index()

# join() : 매개변수로 넘어온 문자열을 해당 문자를 구분자로 나누어서 반환

# 공백제거 : rstrip(), lstrip(), strip()

# replace() : 문자열 교환 예) replace('King', 'Queen’)

# upper() : 해당 문자열을 대문자로 변환
# lower() : 해당 문자열을 소문자로 변환
# count() : 매개변수로 넘어온 문자와 동일한 문자가 해당 문자열 내에 몇 번 등장하는지 그 횟수를 반환
# find() : 매개변수로 넘어온 문자와 동일한 문자가 문자열에서 어디에서 있는지 그 인덱스를 반환


# mylist=[10,20,30,40,16,62,70]
# print(mylist[시작2:끝5-1:skip1일때는생략])
# print(mylist[2:5])   #[30, 40, 16]
# print(mylist[2:5:1]) #[30, 40, 16]
# print(mylist[::2])  #[10, 30, 16, 70]
# print(mylist[::-2]) #[70, 16, 30, 10]
# print('길이 =', len(mylist))
# 에러print('길이 =', mylist.len())


print('hello'.upper()) #대문자
print('HBI'.lower())   #소문자
print('Guido van Rossum1'.split())     #['Guido', 'van', 'Rossum1']
print('Guido van Rossum2'.split(' ')) #['Guido', 'van', 'Rossum1']
print()
print('Apple,Banana,Orange1'.split(','))  #['Apple', 'Banana', 'Orange1']
print('Apple|Banana|Orange2'.split('|'))  #['Apple', 'Banana', 'Orange2']

msg='appleABabaws'
print(msg.count('a'))
print(msg.count('k'))

a,b,hap=4,25,0
hap=a+b
print('{}+{}={}'.format(a,b,hap))
print('{} python!!!'.format('hello'))
print('{0} python!!!'.format('hello'))
print('{0} {1}!!!'.format('hello','python'))
print()
msg='sundaymonday'
print(msg.find('h')) #데이터가 없으면 -1

ret = ','.join(msg)
print(ret)

msg='    sundaymonday    '
print(msg+ 'hb')
print(msg.lstrip()+ 'hb')
print(msg.rstrip()+ 'hb')
print(msg.strip()+ 'hb')
print('ktlgsk'.replace('lg','LG무적'))


print()



