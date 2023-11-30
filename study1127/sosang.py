import pandas as pd
import folium  
from folium.plugins import MarkerCluster
import webbrowser
import os

df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv')
print(df)
'''
#[325880 rows x 39 columns]
 4   상권업종대분류명   325880 non-null  object
 6   상권업종중분류명   325880 non-null  object
 8   상권업종소분류명   325880 non-null  object
 37  경도         325880 non-null  float64
 38  위도         325880 non-null  float64

 이것들을 활용해 데이터에 접근
'''

latlong = df[ ['상권업종대분류명','위도','경도']]
print(latlong)
print('=' *100 ,'\n')

# seoul_coffee = df[df['상권업종중분류명'].str.contains('커피점|카페', na=False)]
seoul_coffee = df.loc[ df['상권업종중분류명'] == '커피점/카페' ]
print(seoul_coffee)
print('=' *100 ,'\n')

latlong = seoul_coffee[ ['위도', '경도', '상호명'] ]
print(latlong)
print('=' *100 ,'\n')

latitude =37.5671 # 위도
longitude = 126.9774 # 경도
m = folium.Map([latitude, longitude], zoom_start=12)        # 기본 위치 위, 경도는 물고 defult임 없으면 에러.

m_cluster = MarkerCluster().add_to(m)
for lat, long, name in zip(latlong['위도'], latlong['경도'], latlong['상호명']):
    folium.Marker(
        location=[lat, long], 
        popup= name,
        icon=folium.Icon(icon='caffee', color='blue')
        ).add_to(m_cluster)

m.save('./data/sosang2.html')
webbrowser.open('file://'+os.path.realpath('./data/sosang2.html'))
print()
print('-' * 100)

