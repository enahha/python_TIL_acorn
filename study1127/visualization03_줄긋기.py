
# 시각화 지도
# https://python-visualization.github.io/folium/latest/getting_started.html
######=============================================

import folium
import webbrowser
import os
import time

m = folium.Map(location=[-71.38, -73.9], zoom_start=11)

trail_coordinates = [
    (-71.351871840295871, -73.655963711222626),
    (-71.374144382613707, -73.719861619751498),
    (-71.391042575973145, -73.784922248007007),
    (-71.400964450973134, -73.851042243124397),
    (-71.402411391077322, -74.050048183880477),
]

folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)

m.save('./data/map3.html')
webbrowser.open(os.path.realpath('./data/map3.html'))
print('지도 테스트2')