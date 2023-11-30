import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc,font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import seaborn as sns
import pandas as pd
import time

pathcsv = './data/navercm.csv'
df = pd.read_csv(pathcsv, encoding='cp949')
print(df)
df.plot(kind='bar', x='nick', y='recomm', legend=True, fontsize=12)
plt.title('df.plot() 빛나는 나나나나 차트 ')
plt.show()

time.sleep(1)
sns.barplot(data=df, x='nick', y='recomm' )
plt.title('seaborn sns.barplot() 빛나는 나나나나 차트 ')
plt.show()














print()
print('-' * 100)