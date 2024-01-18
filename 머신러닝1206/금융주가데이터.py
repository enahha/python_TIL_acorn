import time
import FinanceDataReader as fdr

print('코스피에서 삼성전자가 있는지 확인 검색')
df_krx = fdr.StockListing('KRX')
df_kospi = fdr.StockListing('KOSPI')
## 데이터 프레임 형식으로 나옴
print(df_krx.head())
print(df_kospi.head())
print('krx 거래업체 수>>>', df_krx['Code'].count())
print('kospi 거래업체 수>>>',df_kospi['Code'].count())

# Name으로 '삼성전자' 접근하기
search_name = '삼성전자'
result = df_krx[ df_krx['Name'] == search_name ]
print('\n',result)

# 삼성전자 코드 = 005930, 기간을 가지고 해당 기간의 주가 보기
df = fdr.DataReader('005930', '2023-12-01', '2023-12-05')
print(df)


