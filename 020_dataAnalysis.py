import pandas as pd
import numpy as np

# 创建一个包含随机数的数据框
df = pd.DataFrame({
    'A': np.random.rand(5),
    'B': np.random.rand(5),
    'C': np.random.rand(5)
})

# 计算每一列的均值
mean = df.mean()
print('Mean:\n', mean)

# 计算每一列的中位数
median = df.median()
print('Median:\n', median)

# 计算每一列的标准差
std = df.std()
print('Standard Deviation:\n', std)

# 计算两列之间的相关性
corr = df['A'].corr(df['B'])
print('Correlation between A and B:\n', corr)

"""
使用Pandas和NumPy进行数据分析.

在这段代码中，我们首先导入了Pandas和NumPy库。然后，我们创建了一个名为df的Pandas数据框，它包含了3列随机数。然后我们分别计算了每列的均值、中位数和标准差，并打印出来。最后，我们计算了列'A'和列'B'之间的相关性，并打印出来。
np.random.rand(5)生成一个长度为5的一维数组，数组的每个元素都是[0,1)之间的随机数。
df.mean()计算数据框的列均值。
df.median()计算数据框的列中位数。
df.std()计算数据框的列标准差。
df['A'].corr(df['B'])计算'A'列和'B'列之间的相关性。


在给出的例子中，df 是一个Pandas DataFrame，这是一种二维的、大小可变的、异质的表格数据结构。它类似于Excel表格或SQL表。
在这个例子中，df的大小是 5 行 3 列，原因如下：
我们通过传递一个字典对象给 pd.DataFrame 函数创建了 df。在这个字典中，键（'A', 'B', 'C'）成为了 DataFrame 的列名，值（np.random.rand(5)生成的数组）成为了相应列的数据。因为 np.random.rand(5) 生成的是长度为5的一维数组，所以每列有5个元素，也就是说，数据框有5行。
所以，这个 df DataFrame 的大小是 5 行 3 列。你可以通过 df.shape 属性来查看DataFrame的大小。运行 df.shape 将返回一个元组，元组的第一个元素是行数，第二个元素是列数。在这个例子中，df.shape 将返回 (5, 3)。
"""