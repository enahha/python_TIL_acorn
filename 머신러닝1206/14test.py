
import time
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt

import matplotlib.cbook as cbook
import matplotlib.patches as patches

# C:\Users\hbi\anaconda3\envs\ck\Lib\site-packages\matplotlib\mpl-data\sample_data\36.jpg
with cbook.get_sample_data('36.jpg') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
im.set_clip_path(patch)

ax.axis('off')
plt.show()









print()
print('- ' * 70)
