import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import seaborn as sns



dots = sns.load_dataset('dots')
print(dots) #[848 rows x 5 columns]>
print(dots.describe)
print(dots.info())


print(dots['align'].unique())   #['dots' 'sacc']
print(dots['choice'].unique())  #['T1' 'T2']

sns.lineplot(x='time', y='firing_rate', data=dots)
# sns.lineplot(x='time', y='firing_rate', data=dots, hue='choice')
# sns.lineplot(x='time', y='firing_rate', data=dots, ci=None)
plt.title('dots데이터셋 sns test')
plt.show()
'''
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   align        848 non-null    object
 1   choice       848 non-null    object
 2   time         848 non-null    int64
 3   coherence    848 non-null    float64
 4   firing_rate  848 non-null    float64

    align    choice  time  coherence  firing_rate
0    dots     T1     -80        0.0    33.189967
1    dots     T1     -80        3.2    31.691726
2    dots     T1     -80        6.4    34.279840 

846  sacc     T2     300       25.6    27.009804
847  sacc     T2     300       51.2    30.959302
'''
print()
print('-' * 100)

tips = sns.load_dataset('tips') #ResultSet=dataset=Recordset
print(tips)  # [244 rows x 7 columns]
print(tips.info()) # total_bill   tip  sex  smoker   day    time  size

sns.barplot( data=tips, x='day', y='total_bill')
plt.show()
print('= ' * 70)
# iris붓꽃 
iris = sns.load_dataset('iris')
print(iris[70:90]) #70번째 ~ 89번째 구간 
print(iris.info())

'''
     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
78           6.0          2.9           4.5          1.5  versicolor
79           5.7          2.6           3.5          1.0  versicolor
80           5.5          2.4           3.8          1.1  versicolor
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica
'''


titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.info())
print()
sns.countplot(x='class' ,data=titanic)
plt.title('titanic 클래스별 승객수 ')
plt.show()


print()
print('-' * 100)

