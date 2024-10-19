import matplotlib.pyplot as plt

# 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]

# 创建条形图
plt.bar(labels, values)

# 标题和标签
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图表
plt.show()

"""
看一个关于数据可视化的例子。我们将使用Python的 matplotlib 库来创建一个简单的条形图。

首先，我们导入 matplotlib.pyplot 库。matplotlib 是一个非常强大的 Python 库，用于创建静态、动态、交互式的可视化图表。
然后，我们定义了两个列表 labels 和 values，用于在图表上显示数据。labels 是类别标签，values 是每个类别的值。
plt.bar(labels, values) 创建一个条形图。第一个参数是类别标签，第二个参数是每个类别的值。
plt.title('Bar Chart') 添加图表的标题。
plt.xlabel('Categories') 和 plt.ylabel('Values') 分别添加 x 轴和 y 轴的标签。
最后，plt.show() 显示图表。这会打开一个窗口，显示我们创建的条形图。
这是一个基础的数据可视化例子，matplotlib 的功能远不止这些，你可以创建各种复杂的图表，并进行详细的定制，包括颜色、字体、线型等等。

"""