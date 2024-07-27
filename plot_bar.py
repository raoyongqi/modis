from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import Counter

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

# 计算每个类别的频率
data_flat = data.flatten()
data_counter = Counter(data_flat)

# 按类别顺序整理数据
categories = list(labels_mapping.keys())
frequencies = [data_counter[category] for category in categories]

# 绘制条形图
plt.figure(figsize=(12, 8))
plt.bar([labels_mapping[cat] for cat in categories], frequencies, color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('Land Cover Type')
plt.ylabel('Frequency')
plt.title(f'Distribution of {dataset_name}')
plt.show()
