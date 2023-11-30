# 07mapfilter.py
a = list(range(1,11,1))
print('람다식 결과 =' , (lambda a: a if a%2==0 else None)(36))
print('람다식 결과 =' , list(map(lambda a: a%2==0,a)) )     # [False, True, False, True, False, True, False, True, False, True]
print('람다식 결과 =' , list(filter(lambda a: a%2==0,a)) )  # [2, 4, 6, 8, 10]

print('람다식 결과 =' , map(lambda a: a%2==0,a) )     # <map object at 0x000001FA4FFAB8E0>
print('람다식 결과 =' , filter(lambda a: a%2==0,a) )  # <filter object at 0x000001FA4FFABA00>








print('19일 sunday 저쩌구')
print('19일 sunday 어쩌구')





print()
print('-' * 100)