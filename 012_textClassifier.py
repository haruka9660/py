import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 创建训练数据
train_data = pd.DataFrame({
    'text': [
        'I love this movie',
        'This is an amazing movie',
        'I dislike this movie',
        'This movie is terrible'
    ],
    'label': [
        'positive',
        'positive',
        'negative',
        'negative'
    ]
})

# 创建测试数据
test_data = pd.DataFrame({
    'text': [
        'I enjoy watching this movie',
        'This movie is great'
    ]
})

# 特征提取
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_data['text'])

# 训练分类器
classifier = MultinomialNB()
classifier.fit(train_features, train_data['label'])

# 测试分类器
test_features = vectorizer.transform(test_data['text'])
predictions = classifier.predict(test_features)

# 打印预测结果
for text, prediction in zip(test_data['text'], predictions):
    print(f"{text} - Predicted label: {prediction}")

"""
1 import pandas as pd：导入 Pandas 库，用于数据处理和分析。
2 from sklearn.feature_extraction.text import CountVectorizer：
  从 scikit-learn 库中导入 CountVectorizer 类，用于将文本转换为特征向量。
3 from sklearn.naive_bayes import MultinomialNB：
  从 scikit-learn 库中导入 MultinomialNB 类，用于实现朴素贝叶斯分类器。
4 创建训练数据和测试数据：创建了一个包含文本和标签的训练数据 DataFrame，以及一个只包含文本的测试数据 DataFrame。
  训练数据中的文本是一些电影评论，对应的标签是评论的情感（positive 或 negative）。
5 特征提取：创建一个 CountVectorizer 对象，并使用训练数据的文本列来拟合它，将文本转换为特征向量。
  CountVectorizer 会将文本转换为词袋模型表示，即统计每个文档中每个词的出现次数。
6 训练分类器：创建一个 MultinomialNB 对象，并使用拟合后的特征向量和训练数据的标签来训练分类器。
7 测试分类器：使用训练好的特征提取器，将测试数据的文本列转换为特征向量。然后使用训练好的分类器对特征向量进行预测。
8 打印预测结果：使用循环遍历测试数据的文本和对应的预测标签，将它们打印输出。
这段代码演示了如何使用朴素贝叶斯算法进行文本分类。它使用训练数据训练了一个分类器，并使用特征提取器将测试数据转换为特征向量。最后，通过分类器对测试数据进行预测，并将预测结果打印输出。

"""