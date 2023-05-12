
#  利用svm分类算法对一个测试周期内的一个传感器（以s1为例）的阻值数据进行分类

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_excel('C:/Users/IXZ2SGH/Desktop/tec/voc sensor/data/download/box024/s1.xlsx', header=None)

# 分离数据和标签
X = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM模型训练
clf = SVC(kernel='rbf', gamma='scale')
clf.fit(X_train, y_train)

# 预测测试集
y_pred = clf.predict(X_test)

# 分类准确率
print(f"Accuracy: {clf.score(X_test, y_test)}")


cm = confusion_matrix(y_test, y_pred)
print(cm)
# 绘制混淆矩阵图
#plot_confusion_matrix(clf, X_test, y_test, cmap=plt.cm.Blues)

# 绘制分类决策边界
plt.scatter(X_test[:, 0], y_test, c=y_pred, cmap=plt.cm.Paired, edgecolors='k')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# 读取excel文件
data = pd.read_excel('C:/Users/IXZ2SGH/Desktop/tec/voc sensor/data/download/box024/output_file.xlsx')

# 提取数据和标签
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# 数据标准化
sc = StandardScaler()
X = sc.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# SVM分类
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# 预测测试集结果
y_pred = classifier.predict(X_test)

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(cm)


# acc

from sklearn.metrics import accuracy_score

y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)



'''




