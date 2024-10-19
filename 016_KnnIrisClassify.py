from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

# 载入数据
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 将数据分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 使用k近邻分类器对数据进行训练
knn = KNeighborsClassifier(n_neighbors=3)
"""
这一行代码是用来创建一个K-Nearest Neighbors (KNN) 分类器的实例的。在这个实例中，我们设定最近的3个邻居将被用来决定新数据点的分类。
KNeighborsClassifier 是 sklearn.neighbors 模块中的一个类。这个类用来实现 KNN 分类算法。
n_neighbors=3 是传给 KNeighborsClassifier 构造函数的一个参数。n_neighbors 参数指定了分类决策将基于多少个最近的邻居。在这个例子中，我们设定 n_neighbors=3，表示我们将查看最近的3个邻居的类别来决定新数据点的类别。
当我们用 knn = KNeighborsClassifier(n_neighbors=3) 创建了一个KNN分类器实例后，我们可以使用这个实例的 .fit 方法来训练模型，用 .predict 方法来做预测，以及使用 .score 方法来计算模型在某个数据集上的准确率。

以下是这个类的一些重要方法和参数：
n_neighbors：用于决定类别的邻居数量。
weights：用于决定邻居的权重，选项有 'uniform'（所有邻居的权重相等）和 'distance'（权重和距离成反比）等。
algorithm：用于计算最近邻的算法，如 'ball_tree'，'kd_tree'，'brute'，'auto'。
fit(X, y)：在数据集 (X, y) 上训练模型。
predict(X)：预测数据集 X 的类别。
score(X, y)：计算模型在数据集 (X, y) 上的准确率。
"""
knn.fit(X_train, y_train)

# 在测试集上验证模型的准确度
accuracy = knn.score(X_test, y_test)
print('Model accuracy: ', accuracy)
