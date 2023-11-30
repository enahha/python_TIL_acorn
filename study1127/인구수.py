import pandas as pd
import folium 
from folium import plugins

import matplotlib.pyplot as plt
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
plt.rc('font', family=font_name)

df = pd.read_csv('data/2023인구수.csv', encoding='cp949')
