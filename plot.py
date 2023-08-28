import random
from matplotlib import pyplot as plt

# 准备数据
# 定义横纵坐标
xLabel = ['geneA', 'geneB', 'geneC', 'geneD', 'geneE']
yLabel = ['sample1', 'sample2', 'sample3', 'sample4', 'sample5']
# 定义填充数据
data = []
for i in range(5):
    temp = []
    for j in range(5):
        k = random.randint(0, 100)
        temp.append(k)
    data.append(temp)

# 开始作图
fig = plt.figure()
# 画布
ax = fig.add_subplot(111)
# 坐标刻度
ax.set_yticks(range(len(yLabel)))
ax.set_xticks(range(len(xLabel)))
ax.set_xticklabels(xLabel)
ax.set_yticklabels(yLabel)
# 作图
im = ax.imshow(data)
# 图例
plt.colorbar(im)
plt.show()
