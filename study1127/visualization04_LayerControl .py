
# 시각화 지도
# https://python-visualization.github.io/folium/latest/getting_started.html
######=============================================

import folium
import webbrowser
import os
import time
import requests
import pandas

m = folium.Map(location=[-71.38, -73.9], zoom_start=11)

# # 우리나라
# m = folium.Map(location=[37.5671, 126.9774], zoom_start=14)

m = folium.Map(tiles="cartodbpositron")

geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
).json()

folium.GeoJson(geojson_data, name="hello world").add_to(m)

folium.LayerControl().add_to(m)


m.save('./data/map4.html')
webbrowser.open(os.path.realpath('./data/map4.html'))
print('지역 LayerControl 지도 테스트2')