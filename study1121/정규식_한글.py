import re

msg = '2939239 python 파이썬 가을겨울 hoho rang'

print(re.search('[가-힣]{2,10}', msg))
print(re.search('[가-힣]{2,10}', msg).group())
print(re.findall('[\w]+', msg))