import geopandas as gpd

df = gpd.read_file('sig/sig.shp', encoding='utf-8')
df.head()