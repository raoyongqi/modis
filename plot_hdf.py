from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Patch

# 打开 HDF 文件
file_name = "data/MCD12C1.A2020001.061.2022172062638.hdf"
hdf = SD(file_name, SDC.READ)

# 打印文件中的所有数据集名称
datasets_dic = hdf.datasets()
print("Datasets in the HDF file:")
for idx, sds in enumerate(datasets_dic.keys()):
    print(idx, sds)

# 假设我们选择第一个数据集进行绘制
dataset_name = list(datasets_dic.keys())[0]

# 读取数据集
data = hdf.select(dataset_name)[:]

# 检查数据集信息
print(f"Dataset name: {dataset_name}")
print("Data shape:", data.shape)
print("Data type:", data.dtype)

# 定义标签映射
labels_mapping = {
    1: 'Evergreen Needleleaf Forests',
    2: 'Evergreen Broadleaf Forests',
    3: 'Deciduous Needleleaf Forests',
    4: 'Deciduous Broadleaf Forests',
    5: 'Mixed Forests',
    6: 'Closed Shrublands',
    7: 'Open Shrublands',
    8: 'Woody Savannas',
    9: 'Savannas',
    10: 'Grasslands',
    11: 'Permanent Wetlands',
    12: 'Croplands',
    13: 'Urban and Built-up Lands',
    14: 'Cropland/Natural Vegetation Mosaics',
    15: 'Permanent Snow and Ice',
    16: 'Barren',
    17: 'Water Bodies',
    255: 'Unclassified'
}

# 创建自定义颜色映射
cmap = mcolors.ListedColormap([
    '#006400',  # 常绿针叶林
    '#228B22',  # 常绿阔叶林
    '#8B4513',  # 落叶针叶林
    '#D2691E',  # 落叶阔叶林
    '#9ACD32',  # 混合林
    '#8B0000',  # 封闭灌木地
    '#FF4500',  # 开放灌木地
    '#FFD700',  # 木本稀树草原
    '#ADFF2F',  # 稀树草原
    '#7CFC00',  # 草地
    '#4682B4',  # 永久性湿地
    '#00FFFF',  # 农田
    '#000080',  # 城市和建筑用地
    '#808000',  # 农田/自然植被马赛克
    '#00CED1',  # 永久性冰雪
    '#B22222',  # 荒地
    '#0000FF',  # 水体
    '#A9A9A9'   # 未分类
])

bounds = list(labels_mapping.keys())
norm = mcolors.BoundaryNorm(bounds, cmap.N)

# 创建图例标签
legend_patches = [Patch(color=cmap(i), label=labels_mapping[key]) for i, key in enumerate(bounds)]

# 绘制数据
plt.figure(figsize=(10, 8))
plt.imshow(data, cmap=cmap, norm=norm)
plt.title(f'{dataset_name} from HDF file')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# 添加图例
plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), title='Categories')

plt.show()
from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Patch

# 打开 HDF 文件
file_name = "data/MCD12C1.A2020001.061.2022172062638.hdf"
hdf = SD(file_name, SDC.READ)

# 打印文件中的所有数据集名称
datasets_dic = hdf.datasets()
print("Datasets in the HDF file:")
for idx, sds in enumerate(datasets_dic.keys()):
    print(idx, sds)

# 假设我们选择第一个数据集进行绘制
dataset_name = list(datasets_dic.keys())[0]

# 读取数据集
data = hdf.select(dataset_name)[:]

# 检查数据集信息
print(f"Dataset name: {dataset_name}")
print("Data shape:", data.shape)
print("Data type:", data.dtype)

# 定义标签映射（更新后的）
labels_mapping = {
    0: 'Water Bodies',
    1: 'Evergreen Needleleaf Forests',
    2: 'Evergreen Broadleaf Forests',
    3: 'Deciduous Needleleaf Forests',
    4: 'Deciduous Broadleaf Forests',
    5: 'Mixed Forests',
    6: 'Closed Shrublands',
    7: 'Open Shrublands',
    8: 'Woody Savannas',
    9: 'Savannas',
    10: 'Grasslands',
    11: 'Permanent Wetlands',
    12: 'Croplands',
    13: 'Urban and Built-up Lands',
    14: 'Cropland/Natural Vegetation Mosaics',
    15: 'Permanent Snow and Ice',
    16: 'Barren',
    255: 'Unclassified'
}

# 创建自定义颜色映射
cmap = mcolors.ListedColormap([
    '#0000FF',  # 水体
    '#006400',  # 常绿针叶林
    '#228B22',  # 常绿阔叶林
    '#8B4513',  # 落叶针叶林
    '#D2691E',  # 落叶阔叶林
    '#9ACD32',  # 混合林
    '#8B0000',  # 封闭灌木地
    '#FF4500',  # 开放灌木地
    '#FFD700',  # 木本稀树草原
    '#ADFF2F',  # 稀树草原
    '#7CFC00',  # 草地
    '#4682B4',  # 永久性湿地
    '#00FFFF',  # 农田
    '#000080',  # 城市和建筑用地
    '#808000',  # 农田/自然植被马赛克
    '#00CED1',  # 永久性冰雪
    '#B22222',  # 荒地
    '#A9A9A9'   # 未分类
])

# 将标签映射的值与颜色映射的索引一一对应
bounds = list(labels_mapping.keys())
norm = mcolors.BoundaryNorm(bounds, cmap.N)

# 创建图例标签
legend_patches = [Patch(color=cmap(i), label=labels_mapping[key]) for i, key in enumerate(bounds)]

# 绘制数据
plt.figure(figsize=(10, 8))
plt.imshow(data, cmap=cmap, norm=norm)
plt.title(f'{dataset_name} from HDF file')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# 添加图例
plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), title='Categories')

plt.show()
