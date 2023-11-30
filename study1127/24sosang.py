import pandas as pd


df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv')
print(df)       #[325,880 rows x 39 columns]
print(df.info())
print()
'''
 0   상가업소번호     325880 non-null  int64
 1   상호명        325879 non-null  object
 2   지점명        59613 non-null   object
 3   상권업종대분류코드  325880 non-null  object
 4   상권업종대분류명   325880 non-null  object
 5   상권업종중분류코드  325880 non-null  object
 6   상권업종중분류명   325880 non-null  object
 7   상권업종소분류코드  325880 non-null  object
 8   상권업종소분류명   325880 non-null  object
 9   표준산업분류코드   306407 non-null  object
 10  표준산업분류명    306407 non-null  object
 11  시도코드       325880 non-null  int64
 12  시도명        325880 non-null  object
 13  시군구코드      325880 non-null  int64
 14  시군구명       325880 non-null  object
 15  행정동코드      325880 non-null  int64
 16  행정동명       325235 non-null  object
 17  법정동코드      325880 non-null  int64
 18  법정동명       325880 non-null  object
 19  지번코드       325880 non-null  int64
 20  대지구분코드     325880 non-null  int64
 21  대지구분명      325880 non-null  object
 22  지번본번지      325880 non-null  int64
 23  지번부번지      260409 non-null  float64
 24  지번주소       325880 non-null  object
 25  도로명코드      325880 non-null  int64
 26  도로명        325880 non-null  object
 27  건물본번지      325880 non-null  int64
 28  건물부번지      40995 non-null   float64
 29  건물관리번호     325880 non-null  object
 30  건물명        158286 non-null  object
 31  도로명주소      325880 non-null  object
 32  구우편번호      325880 non-null  int64
 33  신우편번호      325875 non-null  float64
 34  동정보        29108 non-null   object
 35  층정보        204134 non-null  object
 36  호정보        0 non-null       float64
 37  경도         325880 non-null  float64
 38  위도         325880 non-null  float64
'''

star = df[df['상호명'].str.contains('스타벅스|스타 벅스|starbucks', na=False)]
print(star) #[491 rows x 39 columns]
print()

cnt5 = df['상권업종대분류명'].value_counts()
print(cnt5)
print()
'''
상권업종대분류명
음식          119158
소매           95907
생활서비스        58765
학문/교육        23690
부동산          14528
관광/여가/오락      7220
스포츠           4372
숙박            2240
Name: count, dtype: int64
'''


cnt7 = df['상권업종대분류명'].value_counts().index
print(cnt7) #Index(['음식', '소매', '생활서비스', '학문/교육', '부동산', '관광/여가/오락', '스포츠', '숙박'], dtype='object', name='상권업종대분류명')
print()




print()
print('-' * 100)

