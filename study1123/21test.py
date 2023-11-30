import pandas as pd

table = pd.DataFrame( {
        'weight': [80.0, 76.0, 49,  90, 81.7,65 ] ,
        'height': [ 180, 210, 160,  175, 185, 170] ,
        'gender': ['f','m','m', 'f','m','f']
    }
)

print(table)
print()
print(table.sort_values(by='weight', ignore_index=True))
print()

t_group = table.groupby('gender')
# print('t_group 타입 ', type(t_group)) #<class 'pandas.core.groupby.generic.DataFrameGroupBy'>
for k, value in t_group:
    print(k, ':', value)















print()
print('-' * 100)