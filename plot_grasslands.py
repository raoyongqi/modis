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
    10: 'Grasslands'
}

# 定义感兴趣的类别及其颜色
interest_labels = {
    0: '#0000FF',  # Water Bodies
    10: '#7CFC00'  # Grasslands
}

# 创建自定义颜色映射，包含透明颜色
cmap = mcolors.ListedColormap([interest_labels[0], interest_labels[10]])
cmap.set_under('white')  # 设置小于最小值的颜色（未分类区域的颜色）
cmap.set_over('white')   # 设置大于最大值的颜色（未分类区域的颜色）

# 创建新的数据数组，只保留感兴趣的类别，其他类别设置为-1（透明）
filtered_data = np.where(np.isin(data, list(interest_labels.keys())), data, -1)

# 将标签映射的值与颜色映射的索引一一对应
bounds = list(interest_labels.keys()) + [max(interest_labels.keys()) + 1]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

# 创建图例标签
legend_patches = [Patch(color=interest_labels[key], label=labels_mapping[key]) for key in interest_labels.keys()]

# 绘制数据
plt.figure(figsize=(10, 8))
plt.imshow(filtered_data, cmap=cmap, norm=norm)
plt.title(f'{dataset_name} from HDF file (Filtered)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# 添加图例
plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), title='Categories')

plt.show()
