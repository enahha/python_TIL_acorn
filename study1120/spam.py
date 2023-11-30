message = [ 'spam', 'ham', 'spam', 'ham', 'spam' ]

# spam만 추출
## for 문으로 추출
for i in message:
    if i == 'spam':
        print(i, end=' ')

print()

## 리스트 축약식을 적용해서 spam만 추출
print([ i for i in message if i == 'spam' in i])
print([ i for i in message if i == 'spam'])

### 리스트 축약식 과 람다식을 사용
print(list(filter(lambda x: x == 'spam', message)))

### True일경우 1, False일경우 0을 출력
dummy = []
for i in message:
    if i == 'spam':
        tem = 1
        dummy.append(tem)
    else:
        tem = 0
        dummy.append(tem)
print(dummy)
print()

#### 리스트 축약식을 적용
print('리스트 간편 축약식')
print([ 1 if k == 'spam' else 0 for k in message ])