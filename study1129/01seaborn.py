import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import seaborn as sns

print('seaborn 라이브러리 ')
penguins = sns.load_dataset('penguins')
print(penguins)  # [344 rows x 7 columns]
print(penguins.info())
print()
print('-' * 100)

tips = sns.load_dataset('tips') #ResultSet=dataset=Recordset
print(tips)  # [244 rows x 7 columns]
print(tips.info()) # total_bill   tip  sex  smoker   day    time  size
print()

ax = sns.displot(tips['total_bill'])
plt.title('total bill graph')
plt.show()

titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.info())
sns.countplot(x='class' ,data=titanic)
plt.title('titanic 클래스별 승객수 ')
plt.show()









print()
print('-' * 100)