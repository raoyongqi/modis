import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

# 读取 GeoJSON 文件
input_geojson = 'geojson/CN-border-L1.geojson'
gdf = gpd.read_file(input_geojson)

# 转换为实心多边形
def make_solid(geom):
    if geom.is_empty:
        return geom
    if isinstance(geom, Polygon):
        return Polygon(geom.exterior)  # 只保留外边界
    elif isinstance(geom, MultiPolygon):
        return MultiPolygon([Polygon(p.exterior) for p in geom])
    return geom

gdf['geometry'] = gdf['geometry'].apply(make_solid)

# 保存为新的实心 GeoJSON 文件
output_geojson = 'geojson/solid.geojson'
gdf.to_file(output_geojson, driver='GeoJSON')
