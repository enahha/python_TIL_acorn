import re

phone = '''
010-4914-0545   kim
010-2323-6935   lee
010-2943-7890   tea
'''

print(phone)
print(re.sub('-[0-9]{4}-' ,'-****-', phone))        # 가운데 전화번호 ****로 

'''
010-****-0545   kim
010-****-6935   lee
010-****-7890   tea
'''

print()

# 검색을 통해 apple 이란 단어를 출력
data = 'blue apple cherry apple myCom myApple aPPle orange Apple'
print(re.findall('apple', data))        # ['apple', 'apple']

print(re.findall('apple', data, re.I))        # ['apple', 'apple', 'Apple', 'aPPle', 'Apple']

ret= re.compile('apple') 
print(ret.findall(data))             # ['apple', 'apple']

ret= re.compile('apple', re.I)      # re.I 이그노어의 I이다. 대소문자를 구분없이 추출한다.
print(ret.findall(data))                 # ['apple', 'apple', 'Apple', 'aPPle', 'Apple']

