import geopandas as gpd
import matplotlib.pyplot as plt

# 读取生成的 GeoJSON 文件
output_geojson = 'C:/Users/r/desktop/modis/data/clipped_data.geojson'
gdf = gpd.read_file(output_geojson)

# 设置绘图
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# 绘制 GeoJSON 数据
gdf.plot(column='value', ax=ax, legend=True, cmap='viridis')

# 设置标题和轴标签
ax.set_title('Clipped GeoJSON Data')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# 显示绘图
plt.show()
import rasterio
import matplotlib.pyplot as plt

# 读取生成的 TIFF 文件
tiff_file = 'C:/Users/r/desktop/modis/data/clipped_data.tif'

with rasterio.open(tiff_file) as src:
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 读取图像数据
    image = src.read(1)
    
    # 显示图像
    cax = ax.imshow(image, cmap='viridis')
    
    # 添加颜色条
    fig.colorbar(cax, ax=ax, orientation='vertical')
    
    # 设置标题和轴标签
    ax.set_title('Clipped TIFF Data')
    ax.set_xlabel('Column #')
    ax.set_ylabel('Row #')

    plt.show()
