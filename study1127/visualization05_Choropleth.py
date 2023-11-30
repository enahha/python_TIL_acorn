
# 시각화 지도
# https://python-visualization.github.io/folium/latest/getting_started.html
######=============================================
# 등치(Choropleth)는 Pandas DataFrames/Series와 Geo/TopoJSON 도형 간의 데이터를 바인딩하여 생성할 수 있습니다.

import folium
import webbrowser
import os
import time
import requests
import pandas as pd


state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()
state_data = pd.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)
  
print(state_data)
print(state_data.info())    # 열에 관한 정보를 확인

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)

m.save('./data/map5.html')
webbrowser.open(os.path.realpath('./data/map5.html'))
print('미국 각 주별 고용실업율 음영 test')