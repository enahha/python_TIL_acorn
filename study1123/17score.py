import pandas as pd 
#17score.py

path = './data/score.csv'
score = pd.read_csv(path, encoding='cp949')
print(score)
print()
'''
     no  kor  eng  mat  dept
0   101   88   85   86   101
1   102   70   90   92   103
2   103   90   45   55   101
    ~~~~~~~~~~~~~~~~~~~
12  113   82   45   64   101
13  114   88   78   82   101
14  115   56   75   75   103   
'''
# 문제해결 loc,iloc
# 문제1 모든행 kor,eng,mat  
# 문제2 6행~10행포함 kor,eng,mat 
# 참고 print( emp.loc[2:5 , ['Name','No', 'Pay']] )
# 에러 print( score.loc[  , ['kor','eng','mat']])
print( score.loc[ :  , ['kor','eng','mat']])
print()
print( score.loc[ 6:10  , ['kor','eng','mat']])
print()
print( score.iloc[ 6:11  , [1,2,3] ])
print('- ' * 50)

print(score)
print()
# 문제3 dept필드에서 103출력 
print(score[ score['dept']==103])
print()
print(score[ (score.dept)==102])
print()

print(score)
print()
# 문제4 kor필드에서 c최대값추출  max()
print('kor최소값 =', score['kor'].min())
print('kor최대값 =', (score.kor).max())

print()
print('-' * 100)