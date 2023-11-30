import re

msg = 'My best%^3 Frue__%$!@! 987 is 푸르른 blue %37!! Spring winter'
# 문자 추출 최소 3자리에서 5자리까지

print(re.findall('[a-zA-Z]', msg))  # ['M', 'y', 'b', 'e', 's', 't', 'F', 'r', 'u', 'e', 'i', 's', 'b', 'l', 'u', 'e', 'S', 'p', 'r', 'i', 'n', 'g', 'w', 'i', 'n', 't', 'e', 'r']
print(re.findall('[a-zA-Z]{3,5}',msg))  # ['best', 'Frue', 'blue', 'Sprin', 'winte']
print(re.findall('blue',msg))

print(re.findall('[\w]+', msg))     # 한글데이터 포함 word인것을 찾아라
                                    # ['My', 'best', '3', 'Frue__', '987', 'is', '푸르른', 'blue', '37', 'Spring', 'winter']

print(re.findall('[^\w]+', msg))    # 한글데이터 포함 word가 아닌것을 찾아라
                                    # [' ', '%^', ' ', '%$!@! ', ' ', ' ', ' ', ' %', '!! ', ' ']