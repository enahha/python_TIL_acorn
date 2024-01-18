import time
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

# 삼성전자 코드 = 005930, 기간을 가지고 해당 기간의 주가 보기
samsung = fdr.DataReader('005930', '2023-11-01', '2023-12-01')
print(samsung, '\n')
print(samsung.index)
plt.figure(figsize=(14,9))
plt.plot(samsung.index, samsung['Close'])
plt.show()

# 원래 culum이름을 내가 지정한 이름으로 바꿔주기
# data = samsung[ ['Open', 'High', 'Low',  'Close',  'Volume'] ]
samsung.rename(columns={'Open': '개장', 'High':'고가', 'Low':'저가',  'Close':'종가', 'Volume':'거래량', 'Change':'전날대비'}, inplace=True)
print(samsung)