
# 시각화 지도
# https://python-visualization.github.io/folium/latest/getting_started.html
######=============================================
## 0. import folium
## 1. 위도, 경도 위치 파악
## 2. folium 라이브러리의 메소드 Map(location=[위도, 경도], 크기 zoom_start= , 모양 tiles = '')
## 3. save('~~~/~~~.html')로 저장
## 4. 저장된 html 문서를 web브라우저를 통해 열기 webbrowser.open(경로)

import folium
import webbrowser
import os

m = folium.Map(location=[37.5671, 126.9774], zoom_start=15) # tiles='Stamen Terrain
folium.Marker([37.5681, 126.9724], 
              tooltip= 'hello, click me', 
              popup= '우리집', 
              icon= folium.Icon(icon='home', color='red')
              ).add_to(m)

m.save('./data/map2.html')
webbrowser.open(os.path.realpath('./data/map2.html'))
print('서울시청 지도 테스트2')