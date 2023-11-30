import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

names = ['group_a', 'group_b', 'group_c', 'group_d', 'group_e']
values = np.random.randint(30,50,5)
print(values)

plt.scatter(names, values, color='red', s=200, cmap='Purples_r')
for i in np.arange(len(names)):
    plt.text(names[i], values[i]+0.3, values[i])

plt.title('scatter test')
plt.show